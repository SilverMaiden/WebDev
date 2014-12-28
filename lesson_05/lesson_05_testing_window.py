import urllib2

import urllib

import json

from xml.dom import minidom
p = urllib2.urlopen("http://www.nytimes.com/services/xml/rss/nyt/GlobalHome.xml").read()

c = minidom.parseString(p)

#print c

get_elements = c.getElementsByTagName("item")

print len(get_elements)




#print dir(p)

#print p.url

#print p.headers

#print p.headers.items()

#print p.headers['content-type']

#print p.headers['server-type']

