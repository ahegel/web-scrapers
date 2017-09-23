# Web Scrapers
Programs to scrape websites using the [Scrapy](https://scrapy.org/) package in Python.

## Requirements
* Python 2.7
* [Scrapy](https://scrapy.org/)

## Goodreads Reviews Wayback Spider
The spider located in the `goodreadsreviewswayback` folder scrapes the [Internet Archive Wayback Machine](https://archive.org/web/) for archived [Goodreads](https://www.goodreads.com/) book reviews.

### Using the spider
1. To start, you need a list of Wayback Machine URLs to scrape. You can use the included example `wayback_goodreads_urls.txt`, or use `goodreads_urls_to_wayback_urls.py` to generate your own list of Wayback Machine URLs from a list of Goodreads book URLs like the one provided in `goodreads_urls_sample.txt`.
2. Clone or download this repo. If desired, replace `wayback_goodreads_urls.txt` with your own URLs.
3. Navigate to the `goodreadsreviewswayback` folder in a cmd prompt, then enter `scrapy crawl goodreadsreviewswayback -o goodreadsreviewswayback.json` to run the spider. You can replace the .json filename with any descriptive name. The spider will now start running.

### Output
When the spider is finished scraping, you will have two files, a log file (`log.txt`) and a JSON file with a list of JSON objects in this format:

```json
{
  "book_title": ["The Girl with the Dragon Tattoo (Millennium, #1)"],
  "book_author": ["Stieg Larsson", "Reg Keeland"],
  "book_author_url": ["https://www.goodreads.com/author/show/706255.Stieg_Larsson", "https://www.goodreads.com/author/show/2565625.Reg_Keeland"],
  "review_pub_date": ["Nov 09, 2015"],
  "book_genre": ["mystery"],
  "rating": [],
  "body": ["<div class=\"reviewText mediumText description readable\" itemprop=\"reviewBody\">\n"],
  "reading_progress": [],
  "reviewer_name": ["Luc\u00eda"],
  "reviewer_url": ["https://www.goodreads.com/user/show/4260544-luc-a"],
  "reviewer_bookshelves": ["dnf"],
  "reviewer_bookshelf_urls": ["https://www.goodreads.com/review/list/4260544-luc-a?shelf=dnf"],
  "review_likes": [],
  "review_likes_url": [],
  "url": "https://www.goodreads.com/review/show/1438215969?book_show_action=false&from_review_page=2",
  "site": "goodreadsreviews",
  "review_commenters": ["Gerardo", "Luc\u00eda"],
  "review_comments": ["<div class=\"comment u-anchorTarget\" id=\"comment_142601968\">\n", "<div class=\"comment u-anchorTarget\" id=\"comment_142607052\">\n"],
  "review_comment_urls": [
    "https://www.goodreads.com/review/show/1438215969?book_show_action=false&from_review_page=2#comment_142601968", 
    "https://www.goodreads.com/review/show/1438215969?book_show_action=false&from_review_page=2#comment_142607052"],
  "review_comment_dates": [
    "Nov 09, 2015 03:06PM",
    "Nov 09, 2015 05:12PM"],
  "review_commenter_urls": ["https://www.goodreads.com/user/show/40991072-gerardo", "https://www.goodreads.com/user/show/4260544-luc-a"],
  "review_comment_ids": ["comment_142601968", "comment_142607052"]
}
```

You can read this JSON file into a Python program for analysis.

## Goodreads Shelves Wayback Spider
The spider located in the `goodreadsshelveswayback` folder scrapes the [Internet Archive Wayback Machine](https://archive.org/web/) for archived [Goodreads](https://www.goodreads.com/) shelf counts like the ones you see here:

![Goodreads shelf counts](/images/shelf_counts.png)

### Using the spider
1. To start, you need a list of Wayback Machine URLs to scrape. You can use the included example `wayback_goodreads_urls.txt`, or use `goodreads_urls_to_wayback_urls.py` to generate your own list of Wayback Machine URLs from a list of Goodreads book URLs like the one provided in `goodreads_urls_sample.txt`.
2. Clone or download this repo. If desired, replace `wayback_goodreads_urls.txt` with your own URLs.
3. Navigate to the `goodreadsshelveswayback` folder in a cmd prompt, then enter `scrapy crawl goodreadsshelveswayback -o goodreadsshelveswayback.json` to run the spider. You can replace the .json filename with any descriptive name. The spider will now start running.

### Output
When the spider is finished scraping, you will have two files, a log file (`log.txt`) and a JSON file with a list of JSON objects in this format:

```json
{
  "book_title": [
    "Life Code: The New Rules For Winning in the Real World"
  ],
  "people": [
    "22 users",
    "19 users",
    "15 users"
  ],
  "url": "https://web.archive.org/web/20160826202815/http://www.goodreads.com/book/show/17155775-life-code",
  "shelf": [
    "Self Help",
    "Psychology",
    "Nonfiction"
  ],
  "book_url": [
  ],
  "site": "goodreadsshelveswayback",
  "total_shelves": 1,
  "people_url": [
    "https://web.archive.org/web/20160826202815/http://www.goodreads.com/shelf/users/17155775-life-code?shelf=self-help",
    "https://web.archive.org/web/20160826202815/http://www.goodreads.com/shelf/users/17155775-life-code?shelf=psychology",
    "https://web.archive.org/web/20160826202815/http://www.goodreads.com/shelf/users/17155775-life-code?shelf=non-fiction"
  ],
  "shelf_url": [
    "https://web.archive.org/web/20160826202815/http://www.goodreads.com/genres/self-help",
    "https://web.archive.org/web/20160826202815/http://www.goodreads.com/genres/psychology",
    "https://web.archive.org/web/20160826202815/http://www.goodreads.com/genres/non-fiction"
  ]
}
```

You can read this JSON file into a Python program like [`genre_clustering.py`](https://github.com/ahegel/machine-learning-genre) for analysis.