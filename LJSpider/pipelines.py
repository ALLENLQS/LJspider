# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from urllib import request #我们采用urllib.request.urlretrieve
from LJSpider.models import HouseList
class LjspiderPipeline(object):
    def saveData(self,item):
        data = HouseList()
        data.house_title = item.get("house_title")
        data.house_address = item.get("house_address")
        data.house_style = item.get("house_style")
        data.house_size = item.get("house_size")
        data.house_price = item.get("house_price")
        data.save()
    def process_item(self, item, spider):
        self.saveData(item)
        return item
