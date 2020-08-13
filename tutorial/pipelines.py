# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from tutorial.config.config import client


class TutorialPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient(client)
        self.quotes_db = self.client['credit']['quotes']

    def process_item(self, item, spider):
        if spider.name == 'quotes':
            self.quotes_db.update_one({'text': item['text'], 'author': item['author']}, {'$set': item}, upsert=True)
            # spider.crawler.engine.close_spider(spider, '全文结束关闭爬虫')
            return item
        return item

    def __del__(self):
        self.client.close()


class ShenxuPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient(client)
        self.quotes_db = self.client['credit']['shenxu']

    def process_item(self, item, spider):
        if spider.name == 'shenxu':
            self.quotes_db.update_one({'chapter': item['chapter'], 'link': item['link']}, {'$set': item}, upsert=True)
            # spider.crawler.engine.close_spider(spider, '全文结束关闭爬虫')
            return item
        return item

    def __del__(self):
        self.client.close()