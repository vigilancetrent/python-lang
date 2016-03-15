
import urllib
u = urllib.urlopen('http://anyweb site you want.com/path/maybe')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()
print('Wrote hacked.xml')
