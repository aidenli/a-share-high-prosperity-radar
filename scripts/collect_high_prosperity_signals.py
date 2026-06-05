#!/usr/bin/env python3
"""A-share high-prosperity public signal radar MVP.

Public internet signal collection only. It does NOT use Tushare, does NOT make
trading recommendations, and does NOT store secrets. The goal is to create a
stable, auditable signal layer for later local financial/valuation validation.
"""
from __future__ import annotations

import argparse
import email.utils
import hashlib
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

USER_AGENT = "Mozilla/5.0 (compatible; AShareHighProsperityRadar/0.1; +local-research)"


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def to_iso(dt: datetime | None) -> str | None:
    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z") if dt else None


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    value = html.unescape(value.strip())
    for parser in (
        lambda s: email.utils.parsedate_to_datetime(s),
        lambda s: datetime.fromisoformat(s.replace("Z", "+00:00")),
    ):
        try:
            dt = parser(value)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except Exception:
            pass
    m = re.search(r"(20\d{2})[-/.年](\d{1,2})[-/.月](\d{1,2})", value)
    if m:
        try:
            return datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), tzinfo=timezone.utc)
        except Exception:
            return None
    return None


def fetch_url(url: str, timeout: int = 20) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read()
        content_type = resp.headers.get("Content-Type", "")
    charset = "utf-8"
    m = re.search(r"charset=([\w\-]+)", content_type, re.I)
    if m:
        charset = m.group(1)
    for enc in [charset, "utf-8", "gb18030", "gbk"]:
        try:
            return raw.decode(enc)
        except Exception:
            continue
    return raw.decode("utf-8", errors="replace")


class LinkExtractor(HTMLParser):
    def __init__(self, base_url: str):
        super().__init__()
        self.base_url = base_url
        self.links: list[dict[str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            attrs = dict(attrs)
            href = attrs.get("href")
            if href:
                self._href = urllib.parse.urljoin(self.base_url, href)
                self._text = []

    def handle_data(self, data):
        if self._href:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag.lower() == "a" and self._href:
            title = re.sub(r"\s+", " ", html.unescape("".join(self._text))).strip()
            if len(title) >= 6 and not title.startswith(("更多", "首页")):
                self.links.append({"title": title, "url": self._href})
            self._href = None
            self._text = []


@dataclass
class Item:
    id: str
    source_id: str
    source_name: str
    source_level: str
    region: str
    categories: list[str]
    title: str
    url: str
    summary: str
    published_at: str | None
    fetched_at: str
    signal_score: int
    risk_score: int
    net_score: int
    signal_hits: dict[str, list[str]]
    risk_hits: list[str]
    themes: list[str]
    evidence_level: str


def normalize_text(s: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def item_id(url: str, title: str) -> str:
    return hashlib.sha1((url or title).encode("utf-8", errors="ignore")).hexdigest()[:16]


def collect_rss(source: dict[str, Any], limit: int) -> list[dict[str, Any]]:
    content = fetch_url(source["url"])
    root = ET.fromstring(content.encode("utf-8"))
    out = []
    # RSS item
    for node in root.findall(".//item"):
        title = normalize_text(node.findtext("title") or "")
        link = normalize_text(node.findtext("link") or "")
        desc = normalize_text(node.findtext("description") or "")
        date = node.findtext("pubDate") or node.findtext("date")
        if title and link:
            out.append({"title": title, "url": link, "summary": desc, "published_at": parse_date(date)})
        if len(out) >= limit:
            return out
    # Atom entry
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for node in root.findall(".//a:entry", ns) + root.findall(".//entry"):
        title = normalize_text(node.findtext("a:title", namespaces=ns) or node.findtext("title") or "")
        link = ""
        for l in node.findall("a:link", ns) + node.findall("link"):
            link = l.attrib.get("href", "") or (l.text or "")
            if link:
                break
        summary = normalize_text(node.findtext("a:summary", namespaces=ns) or node.findtext("summary") or "")
        date = node.findtext("a:updated", namespaces=ns) or node.findtext("a:published", namespaces=ns) or node.findtext("updated")
        if title and link:
            out.append({"title": title, "url": urllib.parse.urljoin(source["url"], link), "summary": summary, "published_at": parse_date(date)})
        if len(out) >= limit:
            break
    return out


def collect_web(source: dict[str, Any], limit: int) -> list[dict[str, Any]]:
    content = fetch_url(source["url"])
    parser = LinkExtractor(source["url"])
    parser.feed(content)
    seen, out = set(), []
    for link in parser.links:
        u = link["url"].split("#", 1)[0]
        title = link["title"]
        if u in seen or len(title) < 6:
            continue
        seen.add(u)
        # Lightweight date extraction from URL or title.
        dt = parse_date(u) or parse_date(title)
        out.append({"title": title, "url": u, "summary": "", "published_at": dt})
        if len(out) >= limit:
            break
    return out


def hit_keywords(text: str, keywords: list[str]) -> list[str]:
    low = text.lower()
    hits = []
    for kw in keywords:
        if kw.lower() in low:
            hits.append(kw)
    return hits


def score_item(raw: dict[str, Any], source: dict[str, Any], cfg: dict[str, Any], fetched_at: datetime) -> Item:
    text = f"{raw.get('title','')} {raw.get('summary','')}"
    signal_hits = {}
    signal_score = 0
    weights = {
        "demand_strong": 5,
        "supply_tight": 5,
        "price_up": 5,
        "new_product": 3,
        "high_prosperity": 4,
        "policy_support": 2,
    }
    for group, kws in cfg["signal_keywords"].items():
        hits = hit_keywords(text, kws)
        if hits:
            signal_hits[group] = hits[:6]
            signal_score += weights.get(group, 1) * min(len(hits), 3)
    risk_hits = hit_keywords(text, cfg.get("risk_keywords", []))
    risk_score = 4 * min(len(risk_hits), 4)
    themes = []
    for theme, kws in cfg.get("theme_keywords", {}).items():
        if hit_keywords(text, kws):
            themes.append(theme)
    # Source level adds a small credibility prior, but keywords/evidence still dominate.
    level_bonus = {"A1": 3, "A2": 2, "B": 1}.get(source.get("level", ""), 0)
    net_score = signal_score - risk_score + level_bonus
    if net_score >= 18 and len(signal_hits) >= 2:
        evidence_level = "A"
    elif net_score >= 10:
        evidence_level = "B"
    elif net_score >= 5:
        evidence_level = "C"
    else:
        evidence_level = "D"
    return Item(
        id=item_id(raw.get("url", ""), raw.get("title", "")),
        source_id=source["id"],
        source_name=source["name"],
        source_level=source.get("level", ""),
        region=source.get("region", ""),
        categories=source.get("categories", []),
        title=normalize_text(raw.get("title", "")),
        url=raw.get("url", ""),
        summary=normalize_text(raw.get("summary", ""))[:500],
        published_at=to_iso(raw.get("published_at")),
        fetched_at=to_iso(fetched_at) or "",
        signal_score=signal_score,
        risk_score=risk_score,
        net_score=net_score,
        signal_hits=signal_hits,
        risk_hits=risk_hits[:8],
        themes=themes,
        evidence_level=evidence_level,
    )


def merge_stories(items: list[Item]) -> list[dict[str, Any]]:
    buckets: dict[str, list[Item]] = {}
    for it in items:
        key_theme = it.themes[0] if it.themes else "未分类"
        # crude product/event key: theme + first signal group + normalized title prefix
        groups = "+".join(sorted(it.signal_hits.keys())[:2]) or "general"
        key = f"{key_theme}|{groups}"
        buckets.setdefault(key, []).append(it)
    stories = []
    for key, vals in buckets.items():
        vals = sorted(vals, key=lambda x: x.net_score, reverse=True)
        theme, groups = key.split("|", 1)
        sources = sorted({v.source_name for v in vals})
        story_score = sum(max(v.net_score, 0) for v in vals[:5]) + 3 * len(sources)
        stories.append({
            "id": hashlib.sha1(key.encode()).hexdigest()[:12],
            "theme": theme,
            "signal_groups": groups.split("+"),
            "story_score": story_score,
            "source_count": len(sources),
            "sources": sources,
            "top_items": [asdict(v) for v in vals[:8]],
            "risk_flags": sorted({r for v in vals for r in v.risk_hits})[:10],
        })
    return sorted(stories, key=lambda x: x["story_score"], reverse=True)


def write_json(path: Path, data: Any):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


def build_markdown(items: list[Item], stories: list[dict[str, Any]], statuses: list[dict[str, Any]], run_at: datetime) -> str:
    top = sorted(items, key=lambda x: x.net_score, reverse=True)[:30]
    lines = [
        "# A股高景气公开信号雷达 MVP",
        "",
        f"生成时间：{to_iso(run_at)}",
        "",
        "> 说明：本报告只收集公开互联网线索，不使用 Tushare，不构成买卖建议。后续必须经过公司映射、财务、估值、行情和风险反证验证。",
        "",
        "## 1. 本轮源健康",
        "",
        "| 来源 | 状态 | 抓取数 | 有效信号数 | 错误 |",
        "|---|---:|---:|---:|---|",
    ]
    for s in statuses:
        lines.append(f"| {s['source_name']} | {s['status']} | {s['fetched_count']} | {s['relevant_count']} | {s.get('error','')[:80]} |")
    lines += ["", "## 2. 高分信号 Top 30", ""]
    if not top:
        lines.append("本轮没有抓到明显高景气信号。")
    for i, it in enumerate(top, 1):
        lines += [
            f"### {i}. {it.title}",
            f"- 来源：{it.source_name} / {it.source_level} / {it.region}",
            f"- 分数：net={it.net_score}, signal={it.signal_score}, risk={it.risk_score}, 证据等级={it.evidence_level}",
            f"- 主题：{', '.join(it.themes) if it.themes else '未分类'}",
            f"- 命中：{json.dumps(it.signal_hits, ensure_ascii=False)}",
            f"- 风险词：{', '.join(it.risk_hits) if it.risk_hits else '无'}",
            f"- 链接：{it.url}",
            "",
        ]
    lines += ["## 3. 合并故事线", ""]
    for i, st in enumerate(stories[:12], 1):
        lines += [
            f"### {i}. {st['theme']} / {'+'.join(st['signal_groups'])}",
            f"- 故事分：{st['story_score']}",
            f"- 来源数：{st['source_count']}，来源：{', '.join(st['sources'])}",
            f"- 风险提示：{', '.join(st['risk_flags']) if st['risk_flags'] else '无'}",
            "- 代表线索：",
        ]
        for item in st["top_items"][:3]:
            lines.append(f"  - [{item['title']}]({item['url']})（{item['source_name']}，net={item['net_score']}）")
        lines.append("")
    lines += [
        "## 4. 下一步验证规则",
        "",
        "进入股票研究前必须继续验证：",
        "",
        "1. 产品/主题是否能映射到具体 A 股公司；",
        "2. 公司收入中相关产品占比是否足够高；",
        "3. Tushare 财务数据是否验证营收、利润、毛利率、现金流改善；",
        "4. 估值是否已经透支；",
        "5. 是否存在降价、砍单、产能过剩、减持、问询函等反证；",
        "6. 虚拟盘只记录观察和模拟仓位，不直接触发真实交易。",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config/high_prosperity_sources.json")
    ap.add_argument("--output-dir", default="data/processed/high_prosperity_radar")
    ap.add_argument("--report-dir", default="reports/high_prosperity_radar")
    args = ap.parse_args()
    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))
    out_dir = Path(args.output_dir)
    report_dir = Path(args.report_dir)
    run_at = now_utc()
    window_start = run_at - timedelta(hours=int(cfg.get("window_hours", 72)))
    max_items = int(cfg.get("max_items_per_source", 40))

    items: list[Item] = []
    statuses = []
    for src in cfg.get("sources", []):
        start = time.time()
        try:
            raw_items = collect_rss(src, max_items) if src.get("type") == "rss" else collect_web(src, max_items)
            scored = [score_item(r, src, cfg, run_at) for r in raw_items]
            # keep all scored rows for audit, but relevant_count uses net > 0
            items.extend(scored)
            statuses.append({
                "source_id": src["id"], "source_name": src["name"], "status": "ok",
                "fetched_count": len(raw_items), "relevant_count": sum(1 for x in scored if x.net_score > 0),
                "duration_sec": round(time.time() - start, 2), "error": "", "checked_at": to_iso(run_at),
            })
        except Exception as e:
            statuses.append({
                "source_id": src.get("id"), "source_name": src.get("name"), "status": "error",
                "fetched_count": 0, "relevant_count": 0, "duration_sec": round(time.time() - start, 2),
                "error": repr(e), "checked_at": to_iso(run_at),
            })

    # deduplicate by URL/id
    dedup = {}
    for it in items:
        dedup[it.id] = it
    items = list(dedup.values())
    latest = [it for it in items if (parse_date(it.published_at) or run_at) >= window_start]
    relevant = sorted([it for it in items if it.net_score >= 5], key=lambda x: x.net_score, reverse=True)
    stories = merge_stories(relevant)
    stamp = run_at.astimezone(timezone.utc).strftime("%Y%m%d_%H%M%S")

    write_json(out_dir / "latest-signals-all.json", [asdict(x) for x in sorted(items, key=lambda x: x.net_score, reverse=True)])
    write_json(out_dir / "latest-signals-24h.json", [asdict(x) for x in sorted(latest, key=lambda x: x.net_score, reverse=True)])
    write_json(out_dir / "source-status.json", statuses)
    write_json(out_dir / "stories-merged.json", stories)
    write_json(out_dir / "high-prosperity-brief.json", {"generated_at": to_iso(run_at), "top_signals": [asdict(x) for x in relevant[:30]], "stories": stories[:12]})
    write_jsonl(out_dir / "high_prosperity_signals.jsonl", [asdict(x) for x in relevant])
    md = build_markdown(relevant, stories, statuses, run_at)
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / f"high_prosperity_signal_brief_{stamp}.md").write_text(md, encoding="utf-8")
    (report_dir / "latest.md").write_text(md, encoding="utf-8")
    print(json.dumps({
        "generated_at": to_iso(run_at),
        "sources": len(statuses),
        "ok_sources": sum(1 for s in statuses if s["status"] == "ok"),
        "items": len(items),
        "relevant": len(relevant),
        "stories": len(stories),
        "output_dir": str(out_dir),
        "report": str(report_dir / "latest.md"),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
