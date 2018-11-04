# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import log

from scrapy.utils.project import get_project_settings

settings = get_project_settings()


class BaseSpider(CrawlSpider):
    pass


class DemoSpider(CrawlSpider):
    name = 'demo'

    # allowed_domains = ['ailab.cn']
    # start_urls = ['http://tech.ailab.cn']
    allowed_domains = ['w3school.com.cn']
    start_urls = ['http://www.w3school.com.cn/']

    # article_extractor = LinkExtractor(allow=r'article-')
    # pic_extractor = LinkExtractor(allow=r'/uploads/')
    index_extractor = LinkExtractor(allow=r'html/\w+.asp')

    rules = [
        # Rule(article_extractor, callback='parse_item', follow=True),
        # Rule(article_extractor, callback='parse_pic', follow=False),
        Rule(index_extractor, callback='parse_test', follow=True),
    ]

    # @classmethod
    # def parse_item(cls, response):
    #     print settings.get('BOT_NAME')
    #     print response
    #     pass

    @classmethod
    def parse_test(cls, response):
        log.msg(response.url)
        pass
