# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class SubstationPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client.db
        self.table  = self.db.table

    def process_item(self, item, spider):
        self.table.insert(item)
        return item

class SubPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client.db
        self.sub  = self.db.sub

    def process_item(self, item, spider):
        self.sub.insert(item)
        return item
