# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import SubItem


class SubSpider(scrapy.Spider):
    name = 'sub'
    allowed_domains = ['map.baidu.com']
    start_urls = ['http://map.baidu.com/?qt=subways&c=131&format=json&t=1543055378179']

    def parse(self, response):
        text = json.loads(response.text)
        for i in text['subways']['l']:
            sub = SubItem()
            sub_line_info = {
                'sub_line': '',
                'line_info': []
            }
            sub_line_info['sub_line'] = i['l_xmlattr']['lid']
            print(i['l_xmlattr']['lid'])
            for j in i['p']:
                sub_line_info['line_info'].append(j['p_xmlattr']['lb'])
                print(j['p_xmlattr']['lb'])
                sub_line_info['line_info'].append(j['p_xmlattr']['ln'])
                print(j['p_xmlattr']['ln'])
                try:
                    sub_line_info['line_info'].append((j['p_xmlattr']['px'], j['p_xmlattr']['py']))
                except:
                    pass
            sub['sub_line_info'] = sub_line_info
            yield sub
