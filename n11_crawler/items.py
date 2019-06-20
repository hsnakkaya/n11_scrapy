# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    note = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    seller_name = scrapy.Field()
    seller_rating = scrapy.Field()
    seller_url = scrapy.Field()
    pass
