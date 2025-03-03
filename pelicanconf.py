#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Kaushik Rajan'
SITENAME = 'Kaushik Rajan - Research & Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'  # Adjust to your timezone

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Connect With Me links
LINKS = (('CV', '/Kaushik_Rajan_CV.pdf'),
         ('Medium', 'https://kaushikvr06.medium.com'),
         ('GitHub', 'https://github.com/kvr06-ai'),
         ('Email', 'mailto:kaushi@alumni.ncsu.edu'),)

# Remove redundant social section
# SOCIAL = (('GitHub', 'https://github.com/your-github-username'),
#           ('LinkedIn', 'https://linkedin.com/in/your-linkedin-username'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme settings - using Clean Blog theme
THEME = 'themes/pelican-clean-blog'

# Clean Blog theme settings
COLOR_SCHEME_CSS = 'github.css'
HEADER_COVER = ''
HEADER_COLOR = 'black'
SUBTITLE = 'Research & Blog'
FAVICON = ''
SITESUBTITLE = "Research & Blog"
HEADER_COVER_OG = False
USE_CUSTOM_CSS = False

# Disqus and Analytics settings (optional)
DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = ""

# Static paths - include the CV file in the root directory
STATIC_PATHS = ['images', 'pdfs', 'static', '../Kaushik_Rajan_CV.pdf']
EXTRA_PATH_METADATA = {
    '../Kaushik_Rajan_CV.pdf': {'path': 'Kaushik_Rajan_CV.pdf'},
}

# Plugin settings
PLUGINS = ['pelican.plugins.render_math']

# Math settings
MATH_JAX = {
    'align': 'center',
    'process_escapes': True,
    'responsive': True,
}

# Page and article paths
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']

# URL settings
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Clean Blog specific settings
MENUITEMS = [
    ('Blog', '/blog/'),
]

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Social links
SOCIAL = (
    ('github', 'https://github.com/kvr06-ai'),
    ('medium', 'https://kaushikvr06.medium.com'),
    ('envelope', 'mailto:kaushi@alumni.ncsu.edu')
)

# Required templates
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'authors', 'archives')

# Archive settings
DATES_PATH = "archives"
ARCHIVES_URL = "archives.html"
ARCHIVES_SAVE_AS = "archives.html"
YEAR_ARCHIVE_URL = "archives/{date:%Y}/"
YEAR_ARCHIVE_SAVE_AS = "archives/{date:%Y}/index.html"
MONTH_ARCHIVE_URL = "archives/{date:%Y}/{date:%m}/"
MONTH_ARCHIVE_SAVE_AS = "archives/{date:%Y}/{date:%m}/index.html"
DAY_ARCHIVE_URL = "archives/{date:%Y}/{date:%m}/{date:%d}/"
DAY_ARCHIVE_SAVE_AS = "archives/{date:%Y}/{date:%m}/{date:%d}/index.html"
CATEGORIES_URL = "categories.html"
CATEGORIES_SAVE_AS = "categories.html"
TAGS_URL = "tags.html"
TAGS_SAVE_AS = "tags.html"
AUTHORS_URL = "authors.html"
AUTHORS_SAVE_AS = "authors.html"

# Pagination templates
PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'author': None, 'archives': None}
ARCHIVES_EXTENSION = "html"

# Fix for dates_page undefined error
DATES_PAGE = "archives.html"

# SEO Settings
USE_OPEN_GRAPH = True  # Enable Open Graph
OG_LOCALE = 'en_US'    # Open Graph locale
OG_IMAGE = '/static/profile.jpg'  # Default OG image

# Twitter Card settings
TWITTER_CARDS = True
TWITTER_USERNAME = 'kaushikvr06'

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.5,
        'pages': 0.6
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Enable reading time estimation
SHOW_ARTICLE_READTIME = True

# Schema.org representation
SCHEMA_ORG = True 