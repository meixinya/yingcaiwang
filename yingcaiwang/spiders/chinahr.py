# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime
import re
from yingcaiwang.items import YingcaiwangItem
from scrapy_redis.spiders import RedisCrawlSpider
from datetime import timedelta
class ChinahrSpider(RedisCrawlSpider):
    name = 'chinahr'
    allowed_domains = ['chinahr.com']
    # start_urls = ['http://chinahr.com/']
    redis_key = 'chinahrspider:urls'

    rules = (
        Rule(LinkExtractor(allow=r'\w+/jobs/\d+'), follow=True),
        # 海外招聘
        Rule(LinkExtractor(allow=r'pages/index/over\w+.html'), follow=True),
        # 职位详情
        Rule(LinkExtractor(allow=r'/job/\d+.html'), callback='parse_detail', follow=False),
        # Rule(LinkExtractor(allow=r'http://www.chinahr.com/sou/'), follow=True),
        # Rule(LinkExtractor(allow=r'http://www.chinahr.com/job/\w+.html'), callback='parse_detail', follow=True),
        )
    num_pattern = re.compile(r'\d+')
    def parse_detail(self, response):
        item = YingcaiwangItem()
        url = response.url
        pname = response.xpath('//div[@class="base_info"]//span[@class="job_name"]/text()').extract_first()
        money = response.xpath('//div[@class="job_require"]//span[@class="job_price"]/text()').extract()
        if money:
            money = money[0]
            if '-' in money:
                smoney = money.split('-')[0]
                emoney = money.split('-')[1]
            else:
                smoney = money
                emoney = money
        else:
            smoney = '面议'
            emoney = '面议'

        location = response.xpath('//div[@class="job_require"]//span[@class="job_loc"]/text()').extract()
        if location:
            location = location[0]
        else:
            location = '北京'
        # print(location)

        year = response.xpath('//div[@class="job_require"]//span[@class="job_exp"]/text()').extract()
        if '年' in year:
            res = self.num_pattern.search(year)
            syear = res.group()
            eyear = res.group()
        else:
            syear = 0
            eyear = 0

        degree = response.xpath('//div[@class="job_require"]//span[4]/text()').extract()
        if degree:
            degree = degree[0]
        else:
            degree = '大专以上'
        # print(degree)

        ptype = response.xpath('//div[@class="job_require"]//span[3]/text()').extract()
        if ptype:
            ptype = ptype[0]
        else:
            ptype = 'IT'
        # print(ptype)

        tags = response.xpath('//div[@class="job_intro_tag"]/span/text()').extract()
        if tags:
            tags = tags[0]
        else:
            tags = '性别：不限 | 驾照：不要求'
        # print(tags)

        date_pub = response.xpath('//div[@class="job_profile jpadding"]/p/text()').extract()
        if date_pub:
            date_pub = date_pub[0]
            if '昨' in date_pub:
                date_pub = (datetime.datetime.now() - timedelta(days=int(1))).strftime('%Y-%m-%d')
            elif '-' in date_pub:
                date_pub = date_pub
            else:
                date_pub = datetime.datetime.now().strftime('%Y-%m-%d')
        else:
            date_pub = '无'

        advantage = response.xpath('//div[@class="job_fit_tags"]//li/text()').extract()
        if advantage:
            advantage = advantage[0]
        else:
            advantage = '五险一金'
        # print(advantage)

        jobdesc = response.xpath('//div[@class="job_intro_info"]/text()').extract()

        jobdesc = ''.join(jobdesc).replace('\r\n', '').replace(' ', '')
        # print(jobdesc)

        jobaddr = response.xpath('//div[@class="job_require"]//span[@class="job_loc"]/text()').extract()
        if jobaddr:
            jobaddr = jobaddr[0]
        else:
            jobaddr = '无'
        # print(jobaddr)

        company = response.xpath('//div[@class="job-detail-l"]//h4/a/text()').extract()
        if company:
            company = company[0]
        else:
            company = '无'
        # print(company)

        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')
        num = ''

        item['url'] = url
        item['pname'] = pname
        item['smoney'] = smoney
        item['emoney'] = emoney
        item['location'] = location
        item['syear'] = syear
        item['eyear'] = eyear
        item['degree'] = degree
        item['ptype'] = ptype
        item['tags'] = tags
        item['date_pub'] = date_pub
        item['advantage'] = advantage
        item['jobdesc'] = jobdesc
        item['jobaddr'] = jobaddr
        item['company'] = company
        item['crawl_time'] = crawl_time
        item['num'] = num

        yield item
