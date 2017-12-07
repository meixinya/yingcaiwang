# -*- coding: utf-8 -*-

# Scrapy settings for yingcaiwang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'yingcaiwang'

SPIDER_MODULES = ['yingcaiwang.spiders']
NEWSPIDER_MODULE = 'yingcaiwang.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yingcaiwang (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 20

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Host":" www.chinahr.com",
    "Connection":" keep-alive",
    "Cache-Control":" max-age=0",
    "Upgrade-Insecure-Requests":" 1",
    "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language":" zh-CN,zh;q=0.9",
    "Cookie":" chrId=0d2db880cefe4a35b75a51fc4f8e9e07; gr_user_id=167879fa-1627-40bc-8ec9-ca5740216c9b; wmda_uuid=31370ebff55792c826125ac56305d20d; wmda_new_uuid=1; wmda_visited_projects=%3B1732047435009; closeCompletCv=1; als=0; gr_session_id_b64eaae9599f79bd=82e3f182-2505-4d60-a5f4-b0ac541d99d6; _ga=GA1.2.437969455.1511360228; _gid=GA1.2.704510966.1511360228; gtid=3d8823cd4525452084ab39bef508a5d3; gr_session_id_be17cdb1115be298=91eff0e5-013a-4bb4-a87a-26e9341b2117; wmda_session_id=1511360132931-d1a77203-975c-9354; 58tj_uuid=e7641988-7019-40b8-9335-8baf26742ad9; channel=social; new_session=0; new_uv=1; utm_source=; spm=; init_refer=https%253A%252F%252Fwww.sogou.com%252Flink%253Furl%253DDSOYnZeCC_rz88Xns-EirMf2OSjAeUjK; RecentVisitCity=398_beijing; RecentVisitCityFullpathPc=34,398",

}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'yingcaiwang.middlewares.YingcaiwangSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#    'yingcaiwang.middlewares.RandomUserAgent': 1,
#     'yingcaiwang.middlewares.AuthRandomProxy': 2,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

DOWNLOAD_TIMEOUT = 90
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'yingcaiwang.pipelines.YingcaiwangPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# url指纹过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 设置爬虫是否可以中断
SCHEDULER_PERSIST = True

# 设置请求队列类型
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue" # 按优先级入队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"  # 按照队列模式
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack" # 按照栈进行请求的调度

# 配置redis管道文件，权重数字相对最大
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 999,  # redis管道文件，自动把数据加载到redis
}

# AUTH_PROXIES = [
#     {'host': '120.78.166.84:6666', 'auth': 'alice:123456'}
# ]
# redis连接配置
REDIS_HOST = '192.168.103.201'
REDIS_PORT = 6379