# -*- coding: utf-8 -*-

from scrapy import log as logger
from scrapy.spiders import Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.utils.project import get_project_settings
from crawl.spiders.base_spider import BaseSpider

settings = get_project_settings()


class DemoSpider(BaseSpider):
    name = 'demo'

    allowed_domains = ['w3school.com.cn']
    start_urls = ['http://www.w3school.com.cn/']

    index_extractor = LinkExtractor(allow=r'html/\w+.asp')

    rules = [
        Rule(index_extractor, callback='parse_test', follow=True),
    ]

    def __init__(self, *args, **kwargs):
        self.use_driver = True
        super(DemoSpider, self).__init__(*args, **kwargs)

    @classmethod
    def parse_test(cls, response):
        logger.msg(response.url)
        pass
