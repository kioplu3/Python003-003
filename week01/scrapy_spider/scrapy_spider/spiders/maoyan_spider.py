# -*- coding: utf-8 -*-
import scrapy
from scrapy_spider.items import ScrapySpiderItem


class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_spider'
    allowed_domains = ['www.maoyan.com']
    start_urls = ['file:///home/theon/excerise/python/pythontt/Python003-003/week01/test.html']
    # start_urls = ['https://maoyan.com/films?showType=3']
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    # def start_requests(self):
    #     return [scrapy.Request('https://maoyan.com/films?showType=3', callback=self.parse, headers=self.headers)]

    def parse(self, response):
        moive_tags = response.css(".movie-item-hover")
        count = 0
        for index, movie_info in enumerate(moive_tags):
            if count >= 10: return
            item = ScrapySpiderItem()
            item['name'] = movie_info.css('.name::text').get()
            test_list = movie_info.xpath('.//span[@class="hover-tag"]/../text()').re(r'\S+')
            item['categroy'] = test_list[0]
            item['show_date'] = test_list[2]
            yield item
            count += 1
        pass
