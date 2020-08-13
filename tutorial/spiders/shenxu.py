import scrapy
from scrapy.spiders.crawl import Rule, CrawlSpider

from tutorial.items import ShenxuItem
from scrapy.linkextractors import LinkExtractor
import re


class ShenxuSpider(CrawlSpider):
    name = 'shenxu'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/13/13959/']
    rules = [
        Rule(LinkExtractor(allow='.*/13/13959/\d+'), callback='parse'),
    ]

    def parse(self, response):
        shenxu_item = ShenxuItem()
        shenxu_item['chapter'] = self.split_sign(''.join(response.css('div.bookname h1').extract()))
        shenxu_item['content'] = self.split_sign(''.join(response.css('#content').extract()))
        shenxu_item['link'] = response.url
        return shenxu_item

    def split_sign(self,text):
        result = ''
        try:
            result = re.sub(r'<.*?>','',text,flags=re.S)
            result = re.sub(r'\\[a-z|0-9]{1,4}', '', result, flags=re.S)
            result = re.sub(r"'", '', result, flags=re.S)
            result = result.strip()
        except Exception as e:
            self.log(e)
        return result