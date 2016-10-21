# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from dspider.items import DMusicItem
from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider
import logging
import re

class DMusicSpider(CrawlSpider):
    name = "dbmusic"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://book.douban.com/subject/26758235/",
        "https://book.douban.com/tag/%E5%A4%96%E5%9B%BD%E6%96%87%E5%AD%A6",
        "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4",
    ]

    def process_value(value):
        m = re.search(r"https://book.douban.com/subject/[0-9]+/", value)
        if m:
            return m.group(0)

    rules =(
        Rule(LinkExtractor(allow=r'/subject/[0-9]+',process_value = process_value),callback= 'parse_subject', follow= True ),
        Rule(LinkExtractor(allow=r'/tag'), follow= True ),
    )



    def parse_subject(self, response):
        item = DMusicItem()
        item['name'] = response.xpath(r'//span[@property="v:itemreviewed"]/text()').extract()
        item['summary'] = response.xpath(r'//div[@id="link-report"]//p/text()').extract()
        item['author_summary'] = response.xpath(r'//div[@class="indent "]//div[@class="intro"][1]//p/text()').extract()
        item['authors'] = response.xpath(r'//div[@id="info"]//a/text()').extract()
        item['url'] = response.url
        logging.log(logging.INFO,'Crawled Music %s' % response.url)

        yield item
