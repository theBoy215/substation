# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import SubstationItem


class StationSpider(scrapy.Spider):
    name = 'station'
    allowed_domains = ['map.baidu.com']
    start_urls = [
        'http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=alamap&pcevaname=pc4.1&qt=spot&from=webmap&c=131&wd=%E5%9C%B0%E9%93%81%E7%AB%99&wd2=&pn=0&nn=0&db=0&sug=0&addr=0&&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=9.43255632210649&rn=50&tn=B_NORMAL_MAP&auth=EfSWHXGYxJwPPVPGZdc6fv%3D%40w5WcByMKuxHEBVETLHLtDpnSCE%40%40B1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3Guxtdw8E62qvMu8BnlQcWlADEGJM5S7YZzcEWe1GD8zv7u%40ZPuztgwzvf0wd0vyIFC7FUMIyuosSSEb1rZZWuV&u_loc=12959337,4849389&ie=utf-8&b=(12624414.744999954,4781605.970952367;13142627.660238044,4874171.089047605)&t=1543049654653']

    def parse(self, response):
        text = response.text
        content = json.loads(text)
        for i in content['content']:
            sub = SubstationItem()
            addr = i['addr']
            print("地址：", addr)
            area = i['area']
            print("地区：", area)
            area_name = i['area_name']
            print('地区名称：', area_name)
            dic = {
                'b_addr': [],
                'b_name': []
            }
            for j in i['blinfo']:
                dic['b_addr'].append(j['addr'])
                dic['b_name'].append(j['name'])
                print('站名：', dic['b_addr'])
                print('往返站：', dic['b_name'])
            pointXY = (i['diPointX'], i['diPointY'])
            print('坐标:', pointXY)
            sub['addr'] = addr
            sub['area'] = area
            sub['area_name'] = area_name
            sub['b_addr'] = dic['b_addr']
            sub['b_name'] = dic['b_name']
            sub['pointXY'] = pointXY
            yield sub
