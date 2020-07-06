# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'George Goh'
SITENAME = u'George Goh'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["asciidoc_reader"]

#THEME = "simple"
THEME="notmyidea"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}