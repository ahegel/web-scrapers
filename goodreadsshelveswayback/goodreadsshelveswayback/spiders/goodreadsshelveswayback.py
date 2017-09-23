from __future__ import absolute_import
from scrapy.spider import BaseSpider
from scrapy import Request
from goodreadsshelveswayback.items import GoodreadsShelvesWaybackItem
import os
import time
try:
    # Python 2.6-2.7
    from HTMLParser import HTMLParser
except ImportError:
    # Python 3
    from html.parser import HTMLParser


class GoodreadsShelvesWaybackSpider(BaseSpider):
    name = "goodreadsshelveswayback"
    allowed_domains = ["archive.org"]

    # go up three file directory levels to main repo folder for path
    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    infile = "wayback_goodreads_urls.txt"

    start_urls = []
    with open(os.path.join(path, infile)) as f:
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
        item = GoodreadsShelvesWaybackItem()

        item['book_title'] = response.css('div.mainContent > div.mainContentFloat h1:not(.brownBackground) > a:not(.greyText)::text').extract()
        if not item['book_title']:
            item['book_title'] = response.css('div.mainContent > div.mainContentFloat > div.leftContainer > a.bookTitle::text').extract()
        if not item['book_title']:
            item['book_title'] = response.css('div.mainContent > div.mainContentFloat > div.leftContainer h1.bookTitle::text').extract()
        if not item['book_title']:
            item['book_title'] = response.css('h1::text').extract()

        item['book_url'] = response.css('div.mainContent > div.mainContentFloat > h1 > a::attr(href)').extract()
        if not item['book_url']:
            item['book_url'] = response.css('div.mainContent > div.mainContentFloat > div.leftContainer > a.bookTitle::attr(href)').extract()
        if not item['book_url']:
            item['book_url'] = response.css('h1 > a.bookTitle::attr(href)').extract()
        for i, book_url in enumerate(item['book_url']):
            item['book_url'][i] = response.urljoin(book_url)

        item['total_shelves'] = response.css('div.mainContent > div.mainContentFloat > div.leftContainer > span.smallText::text').extract()
        if not item['total_shelves']:
            item['total_shelves'] = 1

        item['shelf'] = response.css('div.mainContent > div.mainContentFloat > div.leftContainer > div.left > div.shelfStat > div > a.mediumText.actionLinkLite:first-of-type::text').extract()
        if not item['shelf']:
            item['shelf'] = response.css('div.mainContent > div.mainContentFloat > div.leftContainer > div.elementList > div > a.mediumText.actionLinkLite:first-of-type::text').extract()
        if not item['shelf']:
            item['shelf'] = response.css('div.mainContent > div.mainContentFloat > div.rightContainer div.elementList > div.left > a.actionLinkLite:first-of-type:not(.smallText):not(.greyText)::text').extract()
        if not item['shelf']:
            item['shelf'] = response.css('div.mainContent > div.mainContentFloat > div.rightContainer > div.myInfoBox > div.myInfoBoxContent > a.actionLinkLite:not(.smallText):not(.greyText)::text').extract()
        if not item['shelf']:
            item['shelf'] = response.css('div.mainContent > div.mainContentFloat > div.rightContainer div.myInfoBox > div.myInfoBoxContent div.left > a.actionLink:not(.smallText):not(.greyText)::text').extract()
        if not item['shelf']:
            item['shelf'] = response.css('div.mainContent > div.mainContentFloat > div.rightContainer a.actionLinkLite:not(.smallText):not(.greyText)::text').extract()
        if not item['shelf']:
            item['shelf'] = response.css('div.mainContent > div.mainContentFloat > div.rightContainer a.actionLink:not(.smallText):not(.greyText)::text').extract()

        item['shelf_url'] = response.css('div.mainContent > div.mainContentFloat > div.leftContainer > div.left > div.shelfStat > div > a.mediumText.actionLinkLite::attr(href)').extract()
        if not item['shelf_url']:
            item['shelf_url'] = response.css('div.mainContent > div.mainContentFloat > div.leftContainer > div.elementList > div > a.mediumText.actionLinkLite::attr(href)').extract()
        if not item['shelf_url']:
            item['shelf_url'] = response.css('div.mainContent > div.mainContentFloat > div.rightContainer div.elementList > div.left > a.actionLinkLite::attr(href)').extract()
        for i, shelf_url in enumerate(item['shelf_url']):
            item['shelf_url'][i] = response.urljoin(shelf_url)

        item['people'] = response.css('div.mainContent > div.mainContentFloat > div.leftContainer > div.left > div.shelfStat > div.smallText > a::text').extract()
        if not item['people']:
            item['people'] = response.css('div.mainContent > div.mainContentFloat > div.leftContainer > div.elementList > div[style*="text-align: right"]::text').extract()
        if not item['people']:
            item['people'] = response.css('div.mainContent > div.mainContentFloat > div.rightContainer div.elementList > div.right > a.actionLinkLite::text').extract()
        if not item['people']:
            item['people'] = response.css('div.mainContent > div.mainContentFloat > div.rightContainer a.actionLinkLite.smallText::text').extract()
        if not item['people']:
            item['people'] = response.css('div.mainContent > div.mainContentFloat > div.rightContainer a.actionLinkLite.greyText::text').extract()

        item['people_url'] = response.css('div.mainContent > div.mainContentFloat > div.leftContainer > div.left > div.shelfStat > div.smallText > a::attr(href)').extract()
        if not item['people_url']:
            item['people_url'] = response.css('div.mainContent > div.mainContentFloat > div.rightContainer div.elementList > div.right > a.actionLinkLite::attr(href)').extract()
        for i, people_url in enumerate(item['people_url']):
            item['people_url'][i] = response.urljoin(people_url)

        # for 2008-ish Goodreads design e.g. https://web.archive.org/web/20081003234647/http://www.goodreads.com/book/show/2164457.Blind_Faith
        if not item['shelf'] and not item['people']:
            item['shelf'] = []
            item['people'] = []
            whole = response.css('div.mainContent > div.mainContentFloat > div.rightContainer a.actionLink.nobold::text').extract()
            for thing in whole:
                temp = thing.split()
                item['shelf'].append(temp[0])
                item['people'].append(temp[1].replace('(', '').replace(')', ''))

        item['url'] = response.url
        item['site'] = GoodreadsShelvesWaybackSpider.name
        yield item
