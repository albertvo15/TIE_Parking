#!/usr/bin/python
import httplib2
import json
import xmljson
h = httplib2.Http(".cache")
resp, content = h.request("http://scpark1.tiesv.org/fid-parkingmanagement", 
    "POST", body="<Query> \
  <Find> \
    <ParkingLot> \
      <LotID> \
        <ne> \
        </ne> \
      </LotID> \
    </ParkingLot> \
  </Find> \
</Query> \
", 
    headers={'content-type':'application/x-www-form-urlencoded'} )
print (content)



from lxml.etree import fromstring, tostring
xml = fromstring(content)
#print (json.dumps(xmljson.gdata.data(xml)))
#print (json.dumps(xmljson.parker.data(xml)))


