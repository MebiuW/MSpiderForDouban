import scrapy
from scrapy.linkextractors import LinkExtractor
from dspider.items import DMovieItem
from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider
import logging
import re

class DMovieSpider(CrawlSpider):
    name = "dbmovie"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://movie.douban.com/subject/26704620/",
        "https://movie.douban.com/chart",
        "https://movie.douban.com/tag",
    ]

    def process_value(value):
        m = re.search(r"https://movie.douban.com/subject/[0-9]+/", value)
        if m:
            return m.group(0)

    rules =(
        Rule(LinkExtractor(allow=r'/subject/[0-9]+',process_value = process_value),callback= 'parse_subject', follow= True ),
        Rule(LinkExtractor(allow=r'/tag',process_value = process_value), follow= True ),
    )



    def parse_subject(self, response):
        item = DMovieItem()
        item['name'] = response.xpath(r'//span[@property="v:itemreviewed"]/text()').extract()
        item['type'] = response.xpath(r'//span[@property="v:genre"]/text()').extract()
        item['summary'] = response.xpath(r'//span[@property="v:summary"]/text()').extract()
        item['score'] = response.xpath(r'//strong[@property="v:average"]/text()').extract()
        item['director'] = response.xpath(r'//a[@rel="v:directedBy"]/text()').extract()
        item['actors'] = response.xpath(r'//span[@class="actor"]//a/text()').extract()
        item['url'] = response.url
        logging.log(logging.INFO,'Crawled %s' % response.url)
        yield item
