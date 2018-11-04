# -*- coding:utf-8 -*-

import fire
from scrapy import cmdline


def start(spider_name=None):
    if not spider_name:
        print 'please input spider name.'
        return
    a = 'scrapy crawl {}'.format(spider_name).split()
    cmdline.execute(a)


if __name__ == '__main__':
    fire.Fire(start)
