# pip install pyshorteners

import pyshorteners
p = pyshorteners.Shortener()
# Pass in your url below
url = ""
print(p.tinyurl.short(url))