# -*- coding: utf-8 -*-

# Scrapy settings for goodreadsreviewswayback project

BOT_NAME = 'goodreadsreviewswayback'

SPIDER_MODULES = ['goodreadsreviewswayback.spiders']
NEWSPIDER_MODULE = 'goodreadsreviewswayback.spiders'

LOG_ENABLED = True
LOG_FILE = 'log.txt'
LOG_STDOUT = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Allison Hegel https://github.com/ahegel'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 32
#CONCURRENT_REQUESTS_PER_IP = 16

DOWNLOAD_TIMEOUT = 300

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
