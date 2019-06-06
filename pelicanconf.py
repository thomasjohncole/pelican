#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Thomas Cole'
SITENAME = 'Thomas Cole'
# do we need this on the local site? seems links break without it
SITEURL = 'http://localhost:8000'
# trying out some URL stuff
INDEX_SAVE_AS = 'blog.html'
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# my modified theme based on tuxlite_tbs
THEME = "/home/tom/code-2019/pelican/themes/tuxlite_tbs_mod"
# display static pages from content/pages/ in the menu
DISPLAY_PAGES_ON_MENU = False
# use this list to get menu links in the correct order
MENUITEMS = (
    ('Home', '/index.html'),
    ('About', '/about-me.html'),
    ('Projects', '/projects.html'),
    ('Blog', '/blog.html'),
    ('Contact', '/contact.html' )
    )

PATH = 'content'
# added this to get a logo in there
STATIC_PATHS = [
    'images',
    'extra',  # this
]
SITELOGO = '/images/logo-03.svg'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# disable cache to see changes
LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/thomasjohncole'),
          ('LinkedIn', 'www.linkedin.com/in/thomas-john-cole'),
          ('Twitter', 'https://twitter.com/thomasjohncole'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True