# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
class MaizieduPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ","
        self.file.write(line)
        return item

    def open_spider(self, spider):
        self.file = codecs.open("out.json", "wb", encoding="utf-8")
        self.file.write('[')

    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()
