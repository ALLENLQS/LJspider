# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LjspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    house_title = scrapy.Field()
    house_address = scrapy.Field()
    house_style = scrapy.Field()
    house_size = scrapy.Field()
    house_price = scrapy.Field()