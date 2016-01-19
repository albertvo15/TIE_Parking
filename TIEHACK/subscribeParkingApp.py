#!/usr/bin/python
import httplib2
import json
import xmljson
h = httplib2.Http(".cache")
resp, content = h.request("http://scpark1.tiesv.org/fid-parkingmanagement", 
    "POST", body='<Query Storage=\"TqlSubscription\"> <Save> <TqlSubscription Label=\"CityParkingApp\" sid="20"> <Topic> * parkingmanagement.management.CityParkingApp.* </Topic> </TqlSubscription> </Save> </Query>', 
    headers={'content-type':'application/x-www-form-urlencoded'} )
print (content)



from lxml.etree import fromstring, tostring
xml = fromstring(content)
#print (json.dumps(xmljson.badgerfish.data(xml)))
#print (json.dumps(xmljson.parker.data(xml)))
print (json.dumps(xmljson.gdata.data(xml)))


