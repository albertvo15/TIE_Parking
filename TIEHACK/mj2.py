#!/usr/bin/python3
import httplib2
h = httplib2.Http(".cache")
resp, content = h.request("http://scpark1.tiesv.org/fid-parkingmanagement", 
    "POST", body="<Query> <Find> <Driver> <Id> <ne> </ne> </Id> </Driver></Find></Query>", 
    headers={'content-type':'application/x-www-form-urlencoded'} )
print (content)
