# -*- coding: utf-8 -*-

from scrapy import log as logger
from scrapy.spiders import CrawlSpider
from scrapy.utils.project import get_project_settings
from scrapy import signals
from selenium import webdriver
from pydispatch import dispatcher

from crawl.utils.header_tool import HeaderTool

settings = get_project_settings()


class BaseSpider(CrawlSpider):
    """爬虫基类"""
    def __init__(self, wait=5, *args, **kwargs):
        self._driver = None
        self.im_wait = wait
        super(BaseSpider, self).__init__(*args, **kwargs)
        # 设置信号量，当收到spider_closed信号时，调用mySpiderCloseHandle方法，关闭chrome
        dispatcher.connect(receiver=self.close_handler,
                           signal=signals.spider_closed)

    @property
    def driver(self):
        if not self._driver:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('lang=zh_CN.UTF-8')
            options.add_argument("user-agent='{}'".format(HeaderTool.get_user_agent()))
            driver = webdriver.Chrome(chrome_options=options)
            driver.implicitly_wait(self.im_wait)
            self._driver = driver
        return self._driver

    # 信号量处理函数：关闭chrome浏览器
    def close_handler(self, spider):
        self.driver.quit()
        logger.msg('{} spider close, close Chrome driver')
