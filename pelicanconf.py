#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Thomas Cole'
SITENAME = 'Thomas Cole'
# do we need this on the local site? seems links break without it
SITEURL = 'http://localhost:8000'
# Save the default index page as blog.html
INDEX_SAVE_AS = 'blog.html'



###########################################
# ADDING STUFF TO MAKE MY CUSTOM THEME WORK - URLS and FILENAMES
ARTICLE_URL = '{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

# Make all the remaining URLs use the trailing slash without file extension

ARTICLE_LANG_URL = '{slug}-{lang}/'
# I know these  work
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# Not sure about these
DRAFT_LANG_URL = 'drafts/{slug}-{lang}/'
DRAFT_PAGE_LANG_URL = 'drafts/pages/{slug}-{lang}/'
DRAFT_PAGE_URL = 'drafts/pages/{slug}/'
DRAFT_URL = 'drafts/{slug}/'
PAGE_LANG_URL = 'pages/{slug}-{lang}/'
STATIC_URL = '{path}/'

# Test these
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/index.html'
DAY_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/{date:%d}/index.html'

YEAR_ARCHIVE_URL = 'archives/{date:%Y}/'
MONTH_ARCHIVE_URL = 'archives/{date:%Y}/{date:%b}/'
DAY_ARCHIVE_URL = 'archives/{date:%Y}/{date:%b}/{date:%d}/'

ARCHIVES_SAVE_AS = 'archives.html'
ARCHIVES_URL = 'archives/'

# additional need to test
# this should just be a list of all the tags
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'

CATEGORYS_URL = 'categories/'
CATEGORYS_SAVE_AS = 'categories/index.html'

# these seem to work now
PAGINATION_PATTERNS = (
(1, '{url}', '{name}{extension}'),
(2, '{url}/{number}', '{name}{number}{extension}'),
)

###############################################


# my modified theme based on tuxlite_tbs
THEME = "/home/tom/code-2019/pelican/themes/tuxlite_tbs_mod"
# display static pages from content/pages/ in the menu
DISPLAY_PAGES_ON_MENU = False
# use this list to get custom menu links
MENUITEMS = (
    ('Home', '/'),
    ('About', '/about-me/'),
    ('Projects', '/projects/'),
    ('Blog', '/blog/'),
    ('Contact', '/contact/' )
    )

PATH = 'content'
# added static paths to get a logo in there and extra
STATIC_PATHS = [
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

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
          ('LinkedIn', 'https://www.linkedin.com/in/thomas-john-cole'),
          ('Twitter', 'https://twitter.com/thomasjohncole'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True