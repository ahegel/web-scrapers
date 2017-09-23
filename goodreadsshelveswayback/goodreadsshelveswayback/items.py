# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from __future__ import absolute_import
import scrapy


class GoodreadsShelvesWaybackItem(scrapy.Item):
    book_title = scrapy.Field()
    book_author = scrapy.Field()
    book_pub_metadata = scrapy.Field()
    book_url = scrapy.Field()
    total_shelves = scrapy.Field()
    shelf = scrapy.Field()
    shelf_url = scrapy.Field()
    people = scrapy.Field()
    people_url = scrapy.Field()
    url = scrapy.Field()
    site = scrapy.Field()