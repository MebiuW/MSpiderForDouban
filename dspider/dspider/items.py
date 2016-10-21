# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DMovieItem(scrapy.Item):
    name = scrapy.Field()
    score = scrapy.Field()
    director = scrapy.Field()
    actors = scrapy.Field()
    type = scrapy.Field()
    summary = scrapy.Field()
    url = scrapy.Field()

class DMusicItem(scrapy.Item):
    name = scrapy.Field()
    score = scrapy.Field()
    type = scrapy.Field()
    authors = scrapy.Field()
    summary = scrapy.Field()
    author_summary = scrapy.Field()
    url = scrapy.Field()

