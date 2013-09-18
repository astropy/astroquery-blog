#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

#MENUITEMS = [(a,'/blog/'+b)  if 'http' not in b else (a,b) for a,b in MENUITEMS]

#SITEURL = 'file://localhost/Volumes/disk5/Users/adam/repos/blog/output'
#SITEURL = ""
#SITEURL = 'http://keflavich.github.io/blog'
FEED_DOMAIN = SITEURL

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
# because apparently nothing works in pelican...
RELATIVE_URLS = False

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
