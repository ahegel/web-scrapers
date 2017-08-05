# -*- coding: utf-8 -*-
"""
Given a list of Goodreads book URLs, gets all available Wayback Machine URLs
using the Wayback CDX Server API (https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server).
"""

import urllib2

infile = "goodreads_urls_sample.txt"
outfile = "wayback_goodreads_urls.txt"

out_urls = []

# get list of Goodreads URLs to find Wayback Machine URLs for
with open(infile, 'r') as f:
    goodreads_urls = f.read().splitlines()

# for each Goodreads URL, add all available Wayback Machine URLs
for i, goodreads_url in enumerate(goodreads_urls):
    cdx_prefix = "http://web.archive.org/cdx/search/cdx?url="
    try:
        index = urllib2.urlopen(cdx_prefix + goodreads_urls[i])
    except:
        print 'error loading page'
        continue
    results = index.read().split('\n')

    # results are in the format: "urlkey","timestamp","original","mimetype","statuscode","digest","length"
    # we just need the timestamp to get the wayback URL
    timestamps = [x.split()[1] for x in results if x]

    wayback_prefix = "https://web.archive.org/web/"
    out_urls += [(wayback_prefix + x + '/' + goodreads_urls[i] + '\n') for x in timestamps]

try:
    out_urls[-1] = out_urls[-1].replace('\n', '')
except:
    print 'make sure out_urls is not empty'
    print out_urls

with open(outfile, 'w') as f:
    f.writelines(out_urls)
