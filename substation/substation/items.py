# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SubstationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id =scrapy.Field()
    addr = scrapy.Field()
    area = scrapy.Field()
    area_name = scrapy.Field()
    b_addr = scrapy.Field()
    b_name = scrapy.Field()
    pointXY = scrapy.Field()

class SubItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id =scrapy.Field()
    sub_line_info = scrapy.Field()

