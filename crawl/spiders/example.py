# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://tech.ailab.cn/article-88209.html']

    def parse(self, response):
        print 233333333333333333333333333333333
        print response.text
        print 233333333333333333333333333333333
        pass
