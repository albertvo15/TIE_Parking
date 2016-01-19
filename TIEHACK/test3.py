#!/usr/bin/python

import json,xmljson

from lxml.etree import fromstring, tostring
xml = fromstring('<p id="1">text</p>')
print json.dumps(xmljson.badgerfish.data(xml))


