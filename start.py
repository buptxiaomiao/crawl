# -*- coding:utf-8 -*-

import fire
from scrapy import cmdline


class App(object):

    @classmethod
    def __start(cls, name):
        cmd = 'scrapy crawl {}'.format(name).split()
        cmdline.execute(cmd)

    @classmethod
    def demo(cls):
        return cls.__start('demo')


if __name__ == '__main__':
    fire.Fire(App)
