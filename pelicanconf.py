#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bhaskar C'
SITENAME = u'CSB'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None    
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('Connect on Linkedin', 'https://www.linkedin.com/in/bhaskar-chakradhar/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Themes
# THEME = "/home/csb/path/to/projects/my_blog/pelican-themes/blue-penguin"

# Add-ons
PLUGIN_PATHS = ['/home/csb/path/to/projects/my_blog/pelican-plugins']
PLUGINS = ["render_math"]

STATIC_PATHS = [
    'images',
    'extra/favicon.ico',
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
