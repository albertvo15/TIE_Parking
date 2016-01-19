#!/usr/bin/python

import xmltodict, json

o = xmltodict.parse('<e> <a>text</a> <a>text</a> </e>')
json.dumps(o) # '{"e": {"a": ["text", "text"]}}'

print (o)
