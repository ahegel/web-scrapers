from __future__ import absolute_import
from scrapy.spider import BaseSpider
from scrapy import Request
from goodreadsreviewswayback.items import GoodreadsReviewsWaybackItem
import time
try:
    # Python 2.6-2.7
    from HTMLParser import HTMLParser
except ImportError:
    # Python 3
    from html.parser import HTMLParser


class GoodreadsReviewsWaybackSpider(BaseSpider):
    name = "goodreadsreviewswayback"
    allowed_domains = ["archive.org"]

    infile = "wayback_goodreads_urls.txt"

    start_urls = []
    with open(infile) as f:
        goodreadsurls = f.read().splitlines()
    for goodreadsurl in goodreadsurls:
        start_urls.append(goodreadsurl)

    def parse(self, response):
        # check if there's a redirect - if so, yield the redirect link instead of the original
        if response.css('p.impatient'):
            redirect = response.css('p.impatient > a::attr(href)').extract()
            redirect_url = response.urljoin(redirect[0])
            yield Request(redirect_url, callback=self.parse_dir_contents)
        else:
            yield Request(response.url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        time.sleep(3)
        item = GoodreadsReviewsWaybackItem()
        item['book_title'] = response.css('h1.bookTitle::text').extract()
        if not item['book_title']:
            item['book_title'] = response.css('h1 > cite::text').extract()
        if not item['book_title']:
            item['book_title'] = response.css('div.title > a::text').extract()
        item['book_author'] = response.css('a.authorName::text').extract()
        if not item['book_author']:
            item['book_author'] = response.css('a.authorName > span::text').extract()
        item['book_author_url'] = response.css('a.authorName::attr(href)').extract()
        item['book_metadata'] = response.css('div#details').extract()
        item['entire_review'] = response.css('div.review').extract()
        item['reviewer_names'] = response.css('div.reviewHeader > a.user::text').extract()
        item['reviewer_urls'] = response.css('div.reviewHeader > a.user::attr(href)').extract()
        count = 0
        for a in item['reviewer_urls']:
            item['reviewer_urls'][count] = response.urljoin(a)
            count += 1
        item['review_bodies'] = response.css('div.reviewText > span > span:last-of-type').extract()
        item['ratings'] = response.css('span.staticStars').extract()
        item['reviews_likes'] = response.css('span.likesCount::text').extract()
        item['review_pub_dates'] = response.css('a.reviewDate::text').extract()
        if not item['review_pub_dates']:
            item['review_pub_dates'] = response.css('div.reviewHeader > div.right > a.createdAt::text').extract()
        item['url'] = response.url
        item['site'] = GoodreadsReviewsWaybackSpider.name
        yield item
