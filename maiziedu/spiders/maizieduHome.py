#-*- coding: UTF-8 -*-
from __future__ import absolute_import
from scrapy.spider import Spider
from scrapy.selector import Selector
from maiziedu.items import MaizieduItem;

class Maiziedu(Spider):
    name = "maizieduHome"
    allowed_domians = ['maiziedu.com']
    start_urls = []

    def __init__(self):
        url = "http://www.maiziedu.com/course/ios/"
        self.start_urls.append(url)

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="lead-img"]')
        items = []
        for site in sites:
            item = MaizieduItem()
            if len(site.xpath('a/@href')) > 0:
                item['link'] = "http://www.maiziedu.com/course" + site.xpath('a/@href').extract()[0];
                item['name'] = site.xpath('a/@title').extract()[0];
                print(item['link'], item['name'])
                items.append(item)
        return items