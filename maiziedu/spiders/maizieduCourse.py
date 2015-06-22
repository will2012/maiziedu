#-*- coding: UTF-8 -*-
from __future__ import absolute_import
from scrapy.spider import Spider
from scrapy.selector import Selector
from maiziedu.items import MaizieduCourseItem;
import json
import sys

class Maiziedu(Spider):
    name = "maizieduCourse"
    allowed_domians = ['maiziedu.com']
    start_urls = []

    def __init__(self):
        filePath = "course.json"
        file_object = open(filePath)
        try:
            jsonStr = file_object.read()
            array = json.loads(jsonStr)
            for item in array:
                link = item['link']
                self.start_urls.append(link)
        finally:
            file_object.close()


    def parse(self, response):
        sel = Selector(response)
        link = sel.re('((http).*?(\.mp4))')[0]
        name = sel.xpath('//title/text()').extract()[0]
        items = []
        item = MaizieduCourseItem()
        item['link'] = link
        item['name'] = name
        items.append(item)
        return items

