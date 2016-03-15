
import os
import time
import sys
import webbrowser
import re
import urllib2

website = urllib2.urlopen('http://192.168.43.173')

html = website.read()
links = re.findall('"()http/ftp)s?://.*?"', html)

print links
