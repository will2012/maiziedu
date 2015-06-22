#-*- coding: UTF-8 -*-
from __future__ import absolute_import
from scrapy.spider import Spider
from scrapy.selector import Selector
from maiziedu.items import MaizieduItem;

class Maiziedu(Spider):
    name = "maiziedu"
    allowed_domians = ['maiziedu.com']
    start_urls = []

    def __init__(self):
        url = "http://www.maiziedu.com/course/course/android/14-2077"
        self.start_urls.append(url)

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@id="playlist"]/ul/li')
        items = []
        for site in sites:
            item = MaizieduItem()
            item['link'] = "http://www.maiziedu.com/course" + site.xpath('a/@href').extract()[0];
            item['name'] = site.xpath('a/text()').extract()[0];
            print(item['link'], item['name'])
            items.append(item)
        return items