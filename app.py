# app.py
import os
import feedparser
from flask import Flask, render_template, jsonify
from flask_caching import Cache
import requests
from datetime import datetime, timezone
import concurrent.futures
import hashlib
from config import THINK_TANKS_CONFIG, get_country_stats, get_category_stats
import time
from email.utils import parsedate_to_datetime

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 600  # 缓存10分钟
cache = Cache(app)


def make_naive(dt):
    """将有时区的时间转换为无时区时间（统一使用UTC）"""
    if dt is None:
        return None
    if dt.tzinfo is not None:
        # 转换为UTC并移除时区信息
        return dt.astimezone(timezone.utc).replace(tzinfo=None)
    return dt


def parse_pub_date(date_string):
    """解析发布时间，返回无时区的datetime对象"""
    if not date_string:
        return None

    try:
        # 尝试使用 email.utils 解析（支持RFC 2822格式）
        # 例如: "Wed, 20 Mar 2024 10:30:00 GMT"
        dt = parsedate_to_datetime(date_string)
        return make_naive(dt)
    except:
        try:
            # 尝试使用 dateutil 解析
            from dateutil import parser
            dt = parser.parse(date_string)
            return make_naive(dt)
        except:
            try:
                # 尝试其他常见格式
                formats = [
                    '%a, %d %b %Y %H:%M:%S %z',
                    '%a, %d %b %Y %H:%M:%S GMT',
                    '%Y-%m-%dT%H:%M:%S%z',
                    '%Y-%m-%d %H:%M:%S',
                    '%Y-%m-%d',
                ]
                for fmt in formats:
                    try:
                        dt = datetime.strptime(date_string, fmt)
                        return make_naive(dt)
                    except:
                        continue
            except:
                pass
    return None


def format_pub_date(date_string):
    """格式化发布时间，显示完整日期时间（包含年份）"""
    if not date_string:
        return '时间未知'

    parsed_date = parse_pub_date(date_string)
    if parsed_date:
        # 格式: 2024年3月20日 10:30
        return parsed_date.strftime('%Y年%m月%d日 %H:%M')
    return '时间未知'


def fetch_feed(feed_info):
    """抓取单个RSS源"""
    articles = []
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(feed_info['rss'], headers=headers, timeout=15)
        if response.status_code != 200:
            print(f"Failed to fetch {feed_info['name']}: status {response.status_code}")
            return []

        feed = feedparser.parse(response.content)
        # 获取最新5篇文章
        for entry in feed.entries[:5]:
            if hasattr(entry, 'link') and hasattr(entry, 'title'):
                # 获取发布时间（优先使用 published，其次 pubDate）
                pub_date_str = entry.get('published', entry.get('pubDate', ''))

                # 解析时间戳用于排序
                pub_timestamp = parse_pub_date(pub_date_str)

                articles.append({
                    'title': entry.title,
                    'link': entry.link,
                    'published_raw': pub_date_str,
                    'published': format_pub_date(pub_date_str),
                    'published_timestamp': pub_timestamp.isoformat() if pub_timestamp else None,
                    'source': feed_info['name'],
                    'source_cn': feed_info['name_cn'],
                    'icon': feed_info.get('icon', ''),
                    'category': feed_info.get('category', '其他'),
                    'country': feed_info.get('country', '其他'),
                    'priority': feed_info.get('priority', 2),
                    'description': feed_info.get('description', '')
                })
    except Exception as e:
        print(f"Error fetching {feed_info['name']}: {e}")
    return articles


def fetch_all_articles():
    """并发抓取所有源，并按时间倒序排列"""
    all_articles = []

    # 按优先级分组
    high_priority = [f for f in THINK_TANKS_CONFIG if f.get('priority', 2) == 1]
    normal_priority = [f for f in THINK_TANKS_CONFIG if f.get('priority', 2) == 2]

    print(f"开始抓取 {len(high_priority)} 个高优先级源和 {len(normal_priority)} 个普通源...")

    # 分批处理，避免请求过多
    batch_size = 10

    # 先处理高优先级
    for i in range(0, len(high_priority), batch_size):
        batch = high_priority[i:i + batch_size]
        print(f"处理高优先级批次 {i // batch_size + 1}/{(len(high_priority) - 1) // batch_size + 1}...")

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_feed = {executor.submit(fetch_feed, feed): feed for feed in batch}
            for future in concurrent.futures.as_completed(future_to_feed):
                articles = future.result()
                all_articles.extend(articles)

        # 批次间休息
        time.sleep(0.5)

    # 再处理普通优先级（只取前20个，避免太多）
    normal_to_fetch = normal_priority[:20]
    for i in range(0, len(normal_to_fetch), batch_size):
        batch = normal_to_fetch[i:i + batch_size]
        print(f"处理普通优先级批次 {i // batch_size + 1}/{(len(normal_to_fetch) - 1) // batch_size + 1}...")

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_feed = {executor.submit(fetch_feed, feed): feed for feed in batch}
            for future in concurrent.futures.as_completed(future_to_feed):
                articles = future.result()
                all_articles.extend(articles)

        time.sleep(0.5)

    # 按时间戳倒序排序（最新的在前）
    def get_timestamp(article):
        timestamp = article.get('published_timestamp')
        if timestamp:
            try:
                # 转换为datetime对象用于比较
                dt = datetime.fromisoformat(timestamp)
                return dt
            except:
                pass
        # 如果没有时间戳，返回一个很早的日期
        return datetime(1970, 1, 1)

    # 过滤掉没有有效时间的文章，放到后面
    articles_with_time = [a for a in all_articles if a.get('published_timestamp')]
    articles_without_time = [a for a in all_articles if not a.get('published_timestamp')]

    # 对有时间的文章排序
    articles_with_time.sort(key=get_timestamp, reverse=True)

    # 合并：有时间的在前（按时间倒序），无时间的在后
    all_articles = articles_with_time + articles_without_time

    print(f"成功抓取 {len(all_articles)} 篇文章")
    print(f"其中 {len(articles_with_time)} 篇有时间信息")
    return all_articles


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/articles')
def get_articles():
    articles = cache.get('articles')
    if articles is None:
        articles = fetch_all_articles()
        if articles:
            cache.set('articles', articles)
    return jsonify(articles or [])


@app.route('/api/sources')
def get_sources():
    """返回所有信息源列表"""
    sources = [{
        'name': s['name'],
        'name_cn': s['name_cn'],
        'category': s.get('category', '其他'),
        'country': s.get('country', '其他'),
        'icon': s.get('icon', ''),
        'description': s.get('description', '')
    } for s in THINK_TANKS_CONFIG]
    return jsonify(sources)


@app.route('/api/stats')
def get_stats():
    """返回统计信息"""
    return jsonify({
        'total_sources': len(THINK_TANKS_CONFIG),
        'country_stats': get_country_stats(),
        'category_stats': get_category_stats()
    })


if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    print(f"已加载 {len(THINK_TANKS_CONFIG)} 个信息源")
    print(f"覆盖国家和地区: {len(get_country_stats())} 个")
    app.run(debug=True, host='0.0.0.0', port=5000)