# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class ShenxuItem(scrapy.Item):
    chapter = scrapy.Field()
    content = scrapy.Field()
    link = scrapy.Field()


class YuanquDetailItem(scrapy.Item):
    entName = scrapy.Field()
    amount = scrapy.Field()
    regisDate = scrapy.Field()
    buScope = scrapy.Field()
    park_name = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    area = scrapy.Field()
    address = scrapy.Field()
    measure_area = scrapy.Field()
    ent_numb = scrapy.Field()
    detail_url = scrapy.Field()