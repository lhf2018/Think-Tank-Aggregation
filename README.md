# Agora

全球智库与政策研究机构 RSS 聚合

[Agora](https://github.com/lhf2018/Think-Tank-Aggregation) 是一个基于 Flask 的 Web 应用，聚合全球智库、国际组织、政策媒体与学术期刊的 RSS 内容，按发布时间倒序展示，支持国家/地区与来源类型筛选、分页浏览。

## 功能特点

- **199 个信息源**，覆盖 **43** 个国家/地区
- **双维度筛选**：国家/地区 × 来源类型（智库、国际组织、认知媒体、学术期刊、经济政策）
- **分页加载**：默认每页 24 条，避免一次性渲染大量卡片
- **后台预热**：启动后在后台抓取 RSS，首屏显示加载状态，完成后自动刷新
- **内存缓存**：抓取结果缓存 10 分钟，降低对源站的压力
- **合规抓取**：优先使用官方 RSS；无 RSS 的智库通过 Google News 站点订阅补充
- **深色界面**：响应式布局，适配桌面与移动端

## 信息源概览

| 来源类型 | 数量 | 说明 |
|----------|------|------|
| 智库 | 170 | 各国/地区政策研究机构（含欧盟智库等） |
| 国际组织 | 12 | 国际危机组织、经合组织等 |
| 认知媒体 | 12 | Foreign Affairs、War on the Rocks 等 |
| 学术期刊 | 3 | Nature、Science、The Lancet 等 |
| 经济政策 | 2 | 彼得森研究所、NBER 等 |

**地区覆盖（部分）**：中国、美国、英国、德国、法国、日本、韩国、印度、巴西、以色列、沙特、澳大利亚，以及泰国、菲律宾、越南、巴基斯坦、伊朗、埃及、尼日利亚、智利、哥伦比亚等。

完整列表见 [`config.py`](./config.py) 中的 `THINK_TANKS_CONFIG`。

## 快速开始

### 环境要求

- Python 3.8+
- 可访问 RSS 源及 Google News（部分源依赖后者）

### 安装与运行

```bash
git clone https://github.com/lhf2018/Think-Tank-Aggregation.git
cd Think-Tank-Aggregation

# 创建虚拟环境（推荐）
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate

pip install -r requirements.txt
python app.py
```

浏览器访问：**http://localhost:5000**

> **首次加载**：应用会在后台并发抓取约 200 个 RSS 源，通常需要 1–2 分钟。页面会自动轮询 `/api/articles/status`，抓取完成后显示文章列表。

## 使用说明

### 筛选

- **国家 / 地区**：按文章来源所在国家筛选（如「中国」「美国」「国际」）
- **来源类型**：按内容性质筛选，与国家级「某某智库」标签解耦
  - `智库` — 各国政策研究机构
  - `国际组织` — 多边机构与非政府组织
  - `认知媒体` — 评论与政策分析网站
  - `学术期刊` — 学术出版物 RSS
  - `经济政策` — 经济类研究机构

两个维度可组合使用，例如「美国 + 认知媒体」。

### 分页

- 底部分页栏切换页码，每页 24 条（API 最大 60 条/页）
- 切换筛选条件时自动回到第 1 页

## 项目结构

```
Think-Tank-Aggregation/
├── app.py              # Flask 应用：抓取、缓存、API
├── config.py           # 信息源配置（THINK_TANKS_CONFIG）
├── requirements.txt    # Python 依赖
├── templates/
│   └── index.html      # 前端页面
├── TODO.md             # 后续规划（SQLite、搜索等）
└── README.md
```

## 配置说明

### 添加信息源

在 `config.py` 的 `THINK_TANKS_CONFIG` 中追加条目：

```python
{
    "name": "Brookings Institution",
    "name_cn": "布鲁金斯学会",
    "rss": "https://example.com/feed.xml",
    "icon": "https://example.com/favicon.ico",
    "category": "美国智库",       # 内部标签，用于映射来源类型
    "country": "美国",
    "priority": 1,               # 1 = 高优先级，2 = 普通
    "description": "美国知名公共政策智库"
}
```

**`category` 与来源类型的映射**（见 `config.py` 中 `get_source_type`）：

| category 值 | 来源类型 |
|-------------|----------|
| `国际组织` | 国际组织 |
| `认知网站` | 认知媒体 |
| `学术期刊` | 学术期刊 |
| `经济政策` | 经济政策 |
| 其他（如 `美国智库`） | 智库 |

无官方 RSS 时，可使用文件顶部的 `GNEWS_CN` / `GNEWS_US` / `GNEWS_SITE` 模板生成 Google News 站点订阅 URL。

### 调整缓存时间

`app.py`：

```python
app.config['CACHE_DEFAULT_TIMEOUT'] = 600  # 秒，默认 10 分钟
```

### 调整并发抓取

`fetch_all_articles()` 中的 `max_workers`（默认 5）和 `batch_size`（默认 10）。

## API 接口

### `GET /api/articles`

分页获取文章列表。

| 参数 | 类型 | 默认 | 说明 |
|------|------|------|------|
| `page` | int | 1 | 页码 |
| `per_page` | int | 24 | 每页条数（最大 60） |
| `country` | string | `all` | 国家/地区，如 `中国`、`美国` |
| `source_type` | string | `all` | `think_tank` / `international` / `media` / `journal` / `policy` |

**响应示例**（抓取完成后）：

```json
{
  "articles": [
    {
      "title": "...",
      "link": "...",
      "published": "2024-03-20 10:30",
      "source": "Brookings Institution",
      "source_cn": "布鲁金斯学会",
      "country": "美国",
      "source_type": "think_tank",
      "source_type_label": "智库"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 24,
    "total": 856,
    "total_pages": 36,
    "has_prev": false,
    "has_next": true
  },
  "loading": false,
  "cached_at": "2024-03-20T12:00:00"
}
```

抓取进行中时 `loading: true`，`articles` 为空数组。

### `GET /api/articles/status`

查询后台抓取状态。

```json
{
  "ready": true,
  "loading": false,
  "total": 856,
  "cached_at": "2024-03-20T12:00:00"
}
```

### `GET /api/sources`

返回全部信息源配置（名称、国家、来源类型等）。

### `GET /api/stats`

返回统计信息：`total_sources`、`country_stats`、`category_stats`、`source_type_labels`。

## 技术栈

| 层级 | 技术 |
|------|------|
| 后端 | Flask、Flask-Caching、feedparser、requests、python-dateutil |
| 前端 | HTML / CSS / 原生 JavaScript（Fetch API） |
| 并发 | `ThreadPoolExecutor` 分批抓取 RSS |

## 常见问题

**Q: 首次打开页面一直 loading？**  
A: 全量抓取约 200 个源需要 1–2 分钟，请等待后台完成；也可查看终端日志确认进度。

**Q: 部分源没有文章？**  
A: RSS 失效、源站限流或 Google News 在本地网络不可达时，该源会被跳过，不影响其他源。

**Q: 筛选后结果为空？**  
A: 检查国家与来源类型组合是否过窄；例如「国际 + 智库」可能几乎没有匹配项。

**Q: 如何强制刷新数据？**  
A: 重启服务或等待 10 分钟缓存过期后重新请求。

**Q: 国内访问 Google News 源不稳定？**  
A: 可在 `config.py` 中将对应条目改为直连 RSS，或使用 `GNEWS_CN` 模板。

## 后续计划

详见 [TODO.md](./TODO.md)，主要包括：

- SQLite 本地持久化（解决每次冷启动全量抓取）
- 增量抓取与源健康度面板
- 标题搜索、去重、`.gitignore` 与部署脚本

## 许可证

MIT License

## 贡献

欢迎提交 Issue 或 Pull Request。添加新信息源时，请优先使用官方 RSS，并在 PR 中说明来源与许可情况。

---

本应用仅供学习与个人阅读聚合使用，请遵守各信息源的版权与使用条款。
