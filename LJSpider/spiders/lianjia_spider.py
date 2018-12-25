#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : ALLEN
# @Time    : 2018/9/18 19:44
# @File    : lianjia_spider.py
# @Software: PyCharm
import scrapy
from LJSpider.items import LjspiderItem
class LiaJiaSpider(scrapy.spiders.Spider):
    name = "LJ"
    def start_requests(self):
        url = "https://cd.lianjia.com/zufang/gaoxin7"
        headers = {
            "Referer":"https://cd.lianjia.com/zufang",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
        }
        yield scrapy.Request(url = url,headers = headers)
    def parse(self,response):
        # self.log(response.body.decode())
        house_list = response.xpath('//ul[@id="house-lst"]/li/div[@class="info-panel"]')
        for house in house_list:
            # t = r.re(r"")
            house_title = house.xpath('h2/a/@title')[0].extract()
            house_address = house.xpath('div/div/a/span/text()')[0].extract()
            house_style = house.xpath('div/div/span/span/text()')[0].extract()
            house_size = house.xpath('div/div/span/text()')[0].extract()
            house_price = house.xpath('div[@class="col-3"]/div/span/text()')[0].extract()
            # result_dict = {
            #     "house_title":house_title,
            #     "house_address": house_address,
            #     "house_style": house_style,
            #     "house_size": house_size,
            #     "house_price": house_price
            # }
            # self.log(result_dict)
            item = LjspiderItem()
            item["house_title"] = house_title
            item["house_address"] = house_address
            item["house_style"] = house_style
            item["house_size"] = house_size
            item["house_price"] = house_price
            # self.log(item)
            yield item
