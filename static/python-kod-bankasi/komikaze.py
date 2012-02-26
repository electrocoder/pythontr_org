"""
	Mirat Can Bayrak / 2009
"""

from urllib import urlopen, urlretrieve
from datetime import date as Date
from datetime import timedelta
from xml.dom import minidom
from os.path import basename
import re

ONE_DAY = timedelta(1)

def asstring(date):
	return "%s%s%s" % (date.year, date.month, date.day)

def nextday(date):
	return date + ONE_DAY

day = Date(2006,1,1)
today = Date.today()

while day != today:
	url = "http://www.komikaze.net/Default.asp?gun=%s" % asstring(day)
	print "checking url :", url
	page = urlopen(url).read()
	images = re.findall('/karikaturler/.*.jpg', page)
	if images:
		for image in images:
			image = "http://www.komikaze.net/komikaze/" + image
			urlretrieve(image, basename(image))
			print image, "downloaded"
	else:
		print "no image found"
	day = nextday(day)
