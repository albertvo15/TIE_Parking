#!/usr/bin/python
import httplib2
import json
import xmljson
h = httplib2.Http(".cache")
resp, content = h.request("http://scpark1.tiesv.org/fid-parkingmanagement", 
    "POST", body="<Query> <Find> <Driver> <Id> <ne> </ne> </Id> </Driver></Find></Query>", 
    headers={'content-type':'application/x-www-form-urlencoded'} )
print (content)



from lxml.etree import fromstring, tostring
xml = fromstring(content)
print (json.dumps(xmljson.badgerfish.data(xml)))


