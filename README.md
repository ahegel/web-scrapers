# Web Scrapers

Programs to scrape websites using the [Scrapy](https://scrapy.org/) package in Python.

## goodreadsreviewswayback

Scrapes the [Internet Archive Wayback Machine](https://archive.org/web/) for archived [Goodreads](https://www.goodreads.com/) book reviews.

To start, you need a list of Wayback Machine URLs to scrape. You can use the included example `wayback_goodreads_urls.txt`, or use `goodreads_urls_to_wayback_urls.py` to generate your own list of Wayback Machine URLs from a list of Goodreads book URLs like the one provided in `goodreads_urls_sample.txt`.
