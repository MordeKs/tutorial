# -*- encoding: utf-8 -*-
"""
@File    : main.py
@Time    : 2020/8/10 15:20
@Author  : Morde
@Software: PyCharm
@Description: 运行爬虫
"""

from scrapy.cmdline import execute

# execute(['scrapy','crawl','quotes','-o','items.json'])

# execute(['scrapy','crawl','shenxu'])
execute(['scrapy','crawl','yuanqu_detail'])