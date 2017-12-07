from scrapy import cmdline
import os
os.chdir('yingcaiwang/spiders')
# cmdline.execute('scrapy crawl wuyoujob'.split())
cmdline.execute('scrapy runspider chinahr.py'.split())
