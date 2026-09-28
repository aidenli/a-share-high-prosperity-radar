# A股高景气公开信号雷达 MVP

生成时间：2026-09-28T16:11:13.623927Z

> 说明：本报告只收集公开互联网线索，不使用 Tushare，不构成买卖建议。后续必须经过公司映射、财务、估值、行情和风险反证验证。

## 1. 本轮源健康

| 来源 | 状态 | 抓取数 | 有效信号数 | 正文抓取 | 错误 |
|---|---:|---:|---:|---:|---|
| 中国政府网-政策 | ok | 30 | 5 | 5 |  |
| 新华社-财经 | ok | 0 | 0 | 0 |  |
| 国家发改委-新闻动态 | ok | 38 | 3 | 3 |  |
| 工信部-新闻动态 | error | 0 | 0 | 0 | URLError(TimeoutError('_ssl.c:999: The handshake operation timed out')) |
| 国家统计局-数据发布 | ok | 40 | 1 | 1 |  |
| Federal Reserve Press Releases | ok | 20 | 0 | 0 |  |
| European Central Bank Press Releases | ok | 15 | 0 | 0 |  |
| IMF News | error | 0 | 0 | 0 | <HTTPError 403: 'Forbidden'> |
| AP Business | error | 0 | 0 | 0 | <HTTPError 403: 'Forbidden'> |
| 巨潮资讯-公告检索页 | ok | 18 | 1 | 1 |  |
| 上交所-披露公告 | ok | 40 | 9 | 10 |  |
| 深交所-上市公司公告 | error | 0 | 0 | 0 | URLError(ConnectionResetError(104, 'Connection reset by peer')) |
| 中国政府采购网-采购公告 | error | 0 | 0 | 0 | <HTTPError 502: 'Bad Gateway'> |
| 海关总署-统计数据 | error | 0 | 0 | 0 | <HTTPError 412: 'Precondition Failed'> |
| 商务部-新闻发布 | ok | 18 | 4 | 3 |  |
| 中国汽车工业协会-行业信息 | ok | 40 | 0 | 0 |  |
| 中国光伏行业协会-新闻动态 | error | 0 | 0 | 0 | URLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certifica |
| 证监会-新闻发布 | error | 0 | 0 | 0 | URLError(TimeoutError('timed out')) |

## 2. 高分信号 Top 30

### 1. 提振消费专项行动 政策集成和综合解读专栏
- 来源：商务部-新闻发布 / A1 / CN
- 分数：net=17, signal=9, risk=0, 证据等级=B, 正文抓取=是
- 主题：消费出海
- 产品映射：家电以旧换新/出海
- 公司映射：格力电器, 海尔智家, 石头科技, 美的集团
- 命中：{"new_product": ["新产品"], "policy_support": ["专项", "以旧换新", "促进", "加快", "推动", "支持", "政策", "新质生产力"]}
- 风险词：无
- 链接：https://www.gov.cn/zhengce/jiedu/tzxfzxxd/index.htm

### 2. 推动大规模设备更新和消费品以旧换新
- 来源：国家发改委-新闻动态 / A1 / CN
- 分数：net=14, signal=6, risk=0, 证据等级=B, 正文抓取=是
- 主题：消费出海
- 产品映射：家电以旧换新/出海
- 公司映射：格力电器, 海尔智家, 石头科技, 美的集团
- 命中：{"policy_support": ["以旧换新", "加快", "推动", "支持", "政策", "行动方案", "设备更新"]}
- 风险词：无
- 链接：https://www.ndrc.gov.cn/xwdt/ztzl/tddgmsbgxhxfpyjhx/

### 3. 交易技术支持专区
- 来源：上交所-披露公告 / A1 / CN
- 分数：net=12, signal=9, risk=0, 证据等级=B, 正文抓取=是
- 主题：AI算力
- 产品映射：无
- 公司映射：无
- 命中：{"new_product": ["上市"], "policy_support": ["support", "专项", "支持"]}
- 风险词：无
- 链接：https://www.sse.com.cn/services/tradingtech/notice/

### 4. 图表：截至2026年8月底全国累计发电装机容量达41.03亿千瓦
- 来源：中国政府网-政策 / A1 / CN
- 分数：net=10, signal=7, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"demand_strong": ["装机"], "policy_support": ["政策"]}
- 风险词：无
- 链接：https://www.gov.cn/zhengce/jiedu/tujie/202609/content_7081984.htm

### 5. 企业上市服务
- 来源：上交所-披露公告 / A1 / CN
- 分数：net=10, signal=7, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"new_product": ["上市"], "policy_support": ["支持", "政策"]}
- 风险词：无
- 链接：https://www.sse.com.cn/services/listingwithsse/home/

### 6. 消费品以旧换新
- 来源：商务部-新闻发布 / A1 / CN
- 分数：net=10, signal=2, risk=0, 证据等级=C, 正文抓取=否
- 主题：消费出海
- 产品映射：家电以旧换新/出海
- 公司映射：格力电器, 海尔智家, 石头科技, 美的集团
- 命中：{"policy_support": ["以旧换新"]}
- 风险词：无
- 链接：http://scyxs.mofcom.gov.cn/xfpyjhx/index.html

### 7. 稳外贸稳外资政策措施
- 来源：商务部-新闻发布 / A1 / CN
- 分数：net=9, signal=6, risk=0, 证据等级=C, 正文抓取=是
- 主题：消费出海
- 产品映射：无
- 公司映射：无
- 命中：{"policy_support": ["促进", "加快", "推动", "政策", "行动方案", "规划"]}
- 风险词：无
- 链接：http://www.mofcom.gov.cn/zcfb/wwmwwzzccs/index.html

### 8. 2026年8月中国采购经理指数运行情况
- 来源：国家统计局-数据发布 / A1 / CN
- 分数：net=8, signal=5, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"demand_strong": ["采购"]}
- 风险词：无
- 链接：https://www.stats.gov.cn/sj/zxfb/202608/t20260831_1965154.html

### 9. 债券发行上市一件事
- 来源：上交所-披露公告 / A1 / CN
- 分数：net=8, signal=5, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"new_product": ["上市"], "policy_support": ["支持"]}
- 风险词：无
- 链接：https://one.sse.com.cn/onething/zqfx/

### 10. 中共中央办公厅 国务院办公厅 中央军委办公厅印发《退役军人服务和保障“十五五”规划》
- 来源：中国政府网-政策 / A1 / CN
- 分数：net=7, signal=4, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"policy_support": ["政策", "规划"]}
- 风险词：无
- 链接：https://www.gov.cn/zhengce/202609/content_7081017.htm

### 11. 国家新闻出版署有关负责同志就《出版业发展“十五五”规划》答记者问
- 来源：中国政府网-政策 / A1 / CN
- 分数：net=7, signal=4, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"policy_support": ["政策", "规划"]}
- 风险词：无
- 链接：https://www.gov.cn/zhengce/202609/content_7081651.htm

### 12. 打通堵点释放潜力 十部门推出促进房车消费若干措施
- 来源：中国政府网-政策 / A1 / CN
- 分数：net=7, signal=4, risk=0, 证据等级=C, 正文抓取=是
- 主题：消费出海
- 产品映射：无
- 公司映射：无
- 命中：{"policy_support": ["促进", "政策"]}
- 风险词：无
- 链接：https://www.gov.cn/zhengce/202609/content_7081497.htm

### 13. 上市公司嵌入
- 来源：巨潮资讯-公告检索页 / A1 / CN
- 分数：net=6, signal=3, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"new_product": ["上市"]}
- 风险词：无
- 链接：http://webapi.cninfo.com.cn/

### 14. 关于上市审核中心
- 来源：上交所-披露公告 / A1 / CN
- 分数：net=6, signal=7, risk=4, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"new_product": ["上市"], "policy_support": ["政策", "规划"]}
- 风险词：终止
- 链接：https://www.sse.com.cn/listing/aboutus/home/

### 15. 上市公司信息
- 来源：上交所-披露公告 / A1 / CN
- 分数：net=6, signal=3, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"new_product": ["上市"]}
- 风险词：无
- 链接：https://www.sse.com.cn/disclosure/listedinfo/announcement/

### 16. 上市公司监管
- 来源：上交所-披露公告 / A1 / CN
- 分数：net=6, signal=3, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"new_product": ["上市"]}
- 风险词：无
- 链接：https://www.sse.com.cn/regulation/supervision/dynamic/

### 17. 发行上市审核监管
- 来源：上交所-披露公告 / A1 / CN
- 分数：net=6, signal=3, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"new_product": ["上市"]}
- 风险词：无
- 链接：https://www.sse.com.cn/regulation/listing/measures/

### 18. 上市公司服务
- 来源：上交所-披露公告 / A1 / CN
- 分数：net=6, signal=3, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"new_product": ["上市"]}
- 风险词：无
- 链接：https://www.sse.com.cn/services/listing/xyzr/

### 19. 关于促进房车消费的若干措施
- 来源：中国政府网-政策 / A1 / CN
- 分数：net=5, signal=2, risk=0, 证据等级=C, 正文抓取=是
- 主题：消费出海
- 产品映射：无
- 公司映射：无
- 命中：{"policy_support": ["促进"]}
- 风险词：无
- 链接：https://www.gov.cn/zhengce/content/202609/content_7081441.htm

### 20. 国家发展改革委发展战略和规划司研究课题入选公告
- 来源：国家发改委-新闻动态 / A1 / CN
- 分数：net=5, signal=2, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"policy_support": ["规划"]}
- 风险词：无
- 链接：https://www.ndrc.gov.cn/xwdt/tzgg/202609/t20260914_1407622.html

### 21. 国家发展改革委发展战略和规划司研究课题征集公告
- 来源：国家发改委-新闻动态 / A1 / CN
- 分数：net=5, signal=2, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"policy_support": ["规划"]}
- 风险词：无
- 链接：https://www.ndrc.gov.cn/xwdt/tzgg/202608/t20260820_1407104.html

### 22. REITs发行上市一件事
- 来源：上交所-披露公告 / A1 / CN
- 分数：net=5, signal=10, risk=8, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"demand_strong": ["合同"], "new_product": ["上市"], "policy_support": ["支持"]}
- 风险词：延期, 终止
- 链接：https://one.sse.com.cn/onething/reits/

### 23. 商务部惠企政策专题
- 来源：商务部-新闻发布 / A1 / CN
- 分数：net=5, signal=2, risk=0, 证据等级=C, 正文抓取=是
- 主题：未分类
- 产品映射：无
- 公司映射：无
- 命中：{"policy_support": ["政策"]}
- 风险词：无
- 链接：https://www.mofcom.gov.cn/swbhqzczt/index.html

## 3. 合并故事线

### 1. 消费出海 / policy_support
- 故事分：56
- 来源数：3，来源：中国政府网-政策, 商务部-新闻发布, 国家发改委-新闻动态
- 产品：家电以旧换新/出海
- 公司：格力电器, 海尔智家, 石头科技, 美的集团
- 风险提示：无
- 代表线索：
  - [推动大规模设备更新和消费品以旧换新](https://www.ndrc.gov.cn/xwdt/ztzl/tddgmsbgxhxfpyjhx/)（国家发改委-新闻动态，net=14）
  - [消费品以旧换新](http://scyxs.mofcom.gov.cn/xfpyjhx/index.html)（商务部-新闻发布，net=10）
  - [稳外贸稳外资政策措施](http://www.mofcom.gov.cn/zcfb/wwmwwzzccs/index.html)（商务部-新闻发布，net=9）

### 2. 未分类 / policy_support
- 故事分：38
- 来源数：3，来源：中国政府网-政策, 商务部-新闻发布, 国家发改委-新闻动态
- 产品：无
- 公司：无
- 风险提示：无
- 代表线索：
  - [中共中央办公厅 国务院办公厅 中央军委办公厅印发《退役军人服务和保障“十五五”规划》](https://www.gov.cn/zhengce/202609/content_7081017.htm)（中国政府网-政策，net=7）
  - [国家新闻出版署有关负责同志就《出版业发展“十五五”规划》答记者问](https://www.gov.cn/zhengce/202609/content_7081651.htm)（中国政府网-政策，net=7）
  - [国家发展改革委发展战略和规划司研究课题入选公告](https://www.ndrc.gov.cn/xwdt/tzgg/202609/t20260914_1407622.html)（国家发改委-新闻动态，net=5）

### 3. 未分类 / new_product
- 故事分：36
- 来源数：2，来源：上交所-披露公告, 巨潮资讯-公告检索页
- 产品：无
- 公司：无
- 风险提示：无
- 代表线索：
  - [上市公司嵌入](http://webapi.cninfo.com.cn/)（巨潮资讯-公告检索页，net=6）
  - [上市公司信息](https://www.sse.com.cn/disclosure/listedinfo/announcement/)（上交所-披露公告，net=6）
  - [上市公司监管](https://www.sse.com.cn/regulation/supervision/dynamic/)（上交所-披露公告，net=6）

### 4. 未分类 / new_product+policy_support
- 故事分：27
- 来源数：1，来源：上交所-披露公告
- 产品：无
- 公司：无
- 风险提示：终止
- 代表线索：
  - [企业上市服务](https://www.sse.com.cn/services/listingwithsse/home/)（上交所-披露公告，net=10）
  - [债券发行上市一件事](https://one.sse.com.cn/onething/zqfx/)（上交所-披露公告，net=8）
  - [关于上市审核中心](https://www.sse.com.cn/listing/aboutus/home/)（上交所-披露公告，net=6）

### 5. 消费出海 / new_product+policy_support
- 故事分：22
- 来源数：1，来源：商务部-新闻发布
- 产品：家电以旧换新/出海
- 公司：格力电器, 海尔智家, 石头科技, 美的集团
- 风险提示：无
- 代表线索：
  - [提振消费专项行动 政策集成和综合解读专栏](https://www.gov.cn/zhengce/jiedu/tzxfzxxd/index.htm)（商务部-新闻发布，net=17）

### 6. AI算力 / new_product+policy_support
- 故事分：15
- 来源数：1，来源：上交所-披露公告
- 产品：无
- 公司：无
- 风险提示：无
- 代表线索：
  - [交易技术支持专区](https://www.sse.com.cn/services/tradingtech/notice/)（上交所-披露公告，net=12）

### 7. 未分类 / demand_strong+policy_support
- 故事分：13
- 来源数：1，来源：中国政府网-政策
- 产品：无
- 公司：无
- 风险提示：无
- 代表线索：
  - [图表：截至2026年8月底全国累计发电装机容量达41.03亿千瓦](https://www.gov.cn/zhengce/jiedu/tujie/202609/content_7081984.htm)（中国政府网-政策，net=10）

### 8. 未分类 / demand_strong
- 故事分：11
- 来源数：1，来源：国家统计局-数据发布
- 产品：无
- 公司：无
- 风险提示：无
- 代表线索：
  - [2026年8月中国采购经理指数运行情况](https://www.stats.gov.cn/sj/zxfb/202608/t20260831_1965154.html)（国家统计局-数据发布，net=8）

### 9. 未分类 / demand_strong+new_product
- 故事分：8
- 来源数：1，来源：上交所-披露公告
- 产品：无
- 公司：无
- 风险提示：延期, 终止
- 代表线索：
  - [REITs发行上市一件事](https://one.sse.com.cn/onething/reits/)（上交所-披露公告，net=5）

## 4. 公司线索映射

### 格力电器（000651.SZ）
- 主题：消费出海
- 产品：家电以旧换新/出海
- 信号数：3，最高分：17，来源：商务部-新闻发布, 国家发改委-新闻动态
- 代表信号：
  - [提振消费专项行动 政策集成和综合解读专栏](https://www.gov.cn/zhengce/jiedu/tzxfzxxd/index.htm)（net=17，B）
  - [推动大规模设备更新和消费品以旧换新](https://www.ndrc.gov.cn/xwdt/ztzl/tddgmsbgxhxfpyjhx/)（net=14，B）
  - [消费品以旧换新](http://scyxs.mofcom.gov.cn/xfpyjhx/index.html)（net=10，C）

### 海尔智家（600690.SH）
- 主题：消费出海
- 产品：家电以旧换新/出海
- 信号数：3，最高分：17，来源：商务部-新闻发布, 国家发改委-新闻动态
- 代表信号：
  - [提振消费专项行动 政策集成和综合解读专栏](https://www.gov.cn/zhengce/jiedu/tzxfzxxd/index.htm)（net=17，B）
  - [推动大规模设备更新和消费品以旧换新](https://www.ndrc.gov.cn/xwdt/ztzl/tddgmsbgxhxfpyjhx/)（net=14，B）
  - [消费品以旧换新](http://scyxs.mofcom.gov.cn/xfpyjhx/index.html)（net=10，C）

### 石头科技（688169.SH）
- 主题：消费出海
- 产品：家电以旧换新/出海
- 信号数：3，最高分：17，来源：商务部-新闻发布, 国家发改委-新闻动态
- 代表信号：
  - [提振消费专项行动 政策集成和综合解读专栏](https://www.gov.cn/zhengce/jiedu/tzxfzxxd/index.htm)（net=17，B）
  - [推动大规模设备更新和消费品以旧换新](https://www.ndrc.gov.cn/xwdt/ztzl/tddgmsbgxhxfpyjhx/)（net=14，B）
  - [消费品以旧换新](http://scyxs.mofcom.gov.cn/xfpyjhx/index.html)（net=10，C）

### 美的集团（000333.SZ）
- 主题：消费出海
- 产品：家电以旧换新/出海
- 信号数：3，最高分：17，来源：商务部-新闻发布, 国家发改委-新闻动态
- 代表信号：
  - [提振消费专项行动 政策集成和综合解读专栏](https://www.gov.cn/zhengce/jiedu/tzxfzxxd/index.htm)（net=17，B）
  - [推动大规模设备更新和消费品以旧换新](https://www.ndrc.gov.cn/xwdt/ztzl/tddgmsbgxhxfpyjhx/)（net=14，B）
  - [消费品以旧换新](http://scyxs.mofcom.gov.cn/xfpyjhx/index.html)（net=10，C）

## 5. 下一步验证规则

进入股票研究前必须继续验证：

1. 产品/主题是否能映射到具体 A 股公司；
2. 公司收入中相关产品占比是否足够高；
3. Tushare 财务数据是否验证营收、利润、毛利率、现金流改善；
4. 估值是否已经透支；
5. 是否存在降价、砍单、产能过剩、减持、问询函等反证；
6. 虚拟盘只记录观察和模拟仓位，不直接触发真实交易。
