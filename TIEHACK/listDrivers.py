#!/usr/bin/python
import httplib2
import json
import xmljson
h = httplib2.Http(".cache")
resp, content = h.request("http://scpark1.tiesv.org/fid-parkingmanagement", 
    "POST", body="<Query> <Find> <Driver> <HomeLocation> <Latitude> <Eq> 33.65316654 </Eq> </Latitude> <Longitude> <Eq> -117.8465224 </Eq> </Longitude> </HomeLocation> </Driver> </Find> </Query> ", 
    headers={'content-type':'application/x-www-form-urlencoded'} )
print (content)



from lxml.etree import fromstring, tostring
xml = fromstring(content)
print (json.dumps(xmljson.parker.data(xml)))


