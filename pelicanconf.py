#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'JQ'
SITENAME = 'Japan Trip 2018'
SITEURL = 'http://localhost:2018'
STATIC_PATHS = ['images', 'pdfs']

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%-m/%-d/%Y'

DEFAULT_CATEGORY = 'general'
DISPLAY_PAGES_ON_MENU = True
THEME = './themes/attila'
HEADER_COVER = 'images/skytree.jpg'
SHOW_FULL_ARTICLE = False

SITESUBTITLE = 'read this stuff plz'

AUTHORS_BIO = {
  "jq": {
    "name": "JQ",
    "cover": "images/arahira.jpg",
    "image": "images/avatar.gif",
    "website": "http://quarl.es",
    "bio": "Inspiring others to use like half their vacation time since 10/2017."
  }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# LINKS = (
#   ('Reddit - Japan Travel Advice Wiki', 'https://www.reddit.com/r/JapanTravel/wiki/traveladvice'),
#   ('Reddit - Japan Travel Advice FAQ', 'https://www.reddit.com/r/JapanTravel/wiki/faqs/japantravel'),
# )

SOCIAL = (
  ('envelope','mailto:john.w.quarles@gmail.com'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
