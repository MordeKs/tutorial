import scrapy
from tutorial.items import TutorialItem
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']# ,'http://quotes.toscrape.com/page/2/'
    # rules = [
    #     Rule(LinkExtractor(allow="http://quotes.toscrape.com/"), follow=False, callback='parse')
    # ]

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        item_nodes = response.css('.quote')
        for item_node in item_nodes:
            tutorial_item = TutorialItem()
            tutorial_item['text'] = ''.join(item_node.css('.text::text').extract()).strip()
            tutorial_item['author'] = ''.join(item_node.css('.author::text').extract()).strip()
            tags_css = item_node.css('.tag')
            tutorial_item['tags'] = [''.join(i.css('::text').extract()).strip() for i in tags_css]
            yield tutorial_item
        self.crawler.engine.close_spider(self, '爬虫任务结束关闭爬虫')