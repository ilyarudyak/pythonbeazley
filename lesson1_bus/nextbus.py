#!/opt/local/bin/python3

import urllib.request
import sys
from xml.etree.ElementTree import XML

if len(sys.argv) != 3:
  raise SystemExit('Usage: nextbus.py route stopid')

# 14787 22
route = sys.argv[1]
stopid = sys.argv[2]
url = 'http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={}&route={}'.format(stopid, route)
print(url)

u = urllib.request.urlopen(url)
data = u.read()
doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)
