# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from __future__ import absolute_import
import scrapy


class GoodreadsReviewsWaybackItem(scrapy.Item):
    book_title = scrapy.Field()
    book_author = scrapy.Field()
    book_metadata = scrapy.Field()
    book_author_url = scrapy.Field()
    entire_review = scrapy.Field()
    review_bodies = scrapy.Field()
    reviewer_names = scrapy.Field()
    reviewer_urls = scrapy.Field()
    ratings = scrapy.Field()
    reviews_likes = scrapy.Field()
    review_pub_dates = scrapy.Field()
    url = scrapy.Field()
    site = scrapy.Field()
