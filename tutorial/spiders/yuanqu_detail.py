from scrapy import Spider
from tutorial.items import YuanquDetailItem
from scrapy.http import Request
import scrapy
import time
import re


class YuanquDetailSpider(scrapy.Spider):
    name = 'yuanqu_detail'
    allowed_domains = ['y.qianzhan.com']
    # start_urls = []
    # area = [11, 12, 13, 14, 15, 21, 22, 23, 31, 32, 33, 34, 36, 37, 41, 42, 43, 44, 45, 46, 50, 51, 52, 53, 54, 61, 62, 63, 64,
    #  65]
    # for i in area:
    #     start_urls.append('https://f.qianzhan.com/yuanqu/diqu/{0}/?pg=1'.format(str(i)))
    start_urls = ['https://f.qianzhan.com/yuanqu/diqu/11/?pg=1']
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'tutorial.middlewares.ProxyMiddleware': 740,
        },
        "DEFAULT_REQUEST_HEADERS": {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            # 'cookie': 'qznewsite.uid=a0i03byshn1g2r55wik3w045; qz.newsite=08EC48A60434DF0AEBE70D032F097E3AB4C33B27BE55B0F40D2781C4350ABFE40B2E5BFB079C800DC6870AA956C55686FA689B01CA75AECE47B9F3AE24DFB0DC21254B73283E97B3226D816E4F3A649FE52FAC3292E1C5CCD9E687565F1B14B0B97F45C9BEC1FB44D041892332D7CAB3C7276FDFE4D651060C41F94E855A4244D6FA8B03; Hm_lvt_311e89cbd04a90da25b9aebdf23be56d=1598410821,1598411061,1598424743,1598424975; Hm_lpvt_311e89cbd04a90da25b9aebdf23be56d=1598424975'
        }
    }

    def parse(self, response):
        page_index = int(''.join(re.findall(r'pg=(\d+)', response.url)))
        url = re.sub(r'pg=(\d+)','',response.url)
        title = ''.join(re.findall(r'\d+', response.css('div.yuanqu-head.mt30 h1::text').extract_first().strip()))
        if title:
            page_count = int(title)//20
        else:
            page_count = 150
        print(page_index, page_count)
        content = response.xpath('//table[@class="company-table"]/tbody/tr')
        for i in content:
            yuanquDetailItem = YuanquDetailItem()
            try:
                yuanquDetailItem['park_name'] = i.xpath('td[2]//text()').extract_first().strip()
            except:
                yuanquDetailItem['park_name'] = ''
            try:
                yuanquDetailItem['province'] = i.xpath('td[3]//text()').extract_first().strip()
            except:
                yuanquDetailItem['province'] = ''
            try:
                yuanquDetailItem['city'] = i.xpath('td[4]//text()').extract_first().strip()
            except:
                yuanquDetailItem['city'] = ''
            try:
                yuanquDetailItem['area'] = i.xpath('td[5]//text()').extract_first().strip()
            except:
                yuanquDetailItem['area'] = ''
            try:
                yuanquDetailItem['address'] = i.xpath('td[6]//text()').extract_first().strip()
            except:
                yuanquDetailItem['address'] = ''
            try:
                yuanquDetailItem['measure_area'] = i.xpath('td[7]//text()').extract_first().strip()
            except:
                yuanquDetailItem['measure_area'] = ''
            try:
                yuanquDetailItem['ent_numb'] = i.xpath('td[8]//text()').extract_first().strip()
            except:
                yuanquDetailItem['ent_numb'] = ''
            try:
                yuanquDetailItem['detail_url'] = i.xpath('td[9]//a/@href').extract_first().strip()
            except:
                yuanquDetailItem['detail_url'] = ''
            # if yuanquDetailItem['detail_url']:
            #     yield Request(yuanquDetailItem['detail_url'],
            #                   callback=self.detail_parse,
            #                   meta={'item': yuanquDetailItem},
            #                   priority=10,
            #                   dont_filter=True
            #                   )
                # time.sleep(5)
            print(yuanquDetailItem)
        if page_index <= page_count:
            page_index += 1
            next_page = url+'pg='+str(page_index)
            print(f'下一页:', page_index)
            yield Request(next_page,
                          callback=self.parse,
                          dont_filter=True,
                          )
            time.sleep(2)

    def detail_parse(self, response):
        yuanquDetailItem = response.meta['item']
        table_info = response.css('table.dataTable.f14 tbody tr')
        for i in table_info:
            yuanquDetailItem['entName'] = i.css('tr td:nth-child(2) *::text').extract_first().strip()
            yuanquDetailItem['amount'] = i.css('tr td:nth-child(3) *::text').extract_first()
            yuanquDetailItem['regisDate'] = i.css('tr td:nth-child(4) *::text').extract_first().strip()
            yuanquDetailItem['buScope'] = i.css('tr td:nth-child(5) *::text').extract_first().strip()
            # yield yuanquDetailItem
