import urllib2

body = urllib2.urlopen('http://www.cut.ac.zw')
print body.read()
