#!/usr/bin/python3.1
import json
import urllib.request
import urllib.parse
import hashlib
import random
import re
#import urllib


def showsome(searchfor):
  query = urllib.parse.urlencode({'q': searchfor})
  url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&{0}".format(query)
  print(url)
  search_response = urllib.request.urlopen(url)
  search_results = search_response.read().decode("windows-1251")
  results = json.loads(search_results)
#  print(results)
  data = results["responseData"]
  print("Total results: {0}".format(data["cursor"]["estimatedResultCount"]))
  hits = data["results"]
  print("Top {0} hits:".format(len(hits)))
#  print(hits)
  for h in hits:
    print("  {0}".format(h["url"]))
  print("For more results, see {0}".format(data["cursor"]["moreResultsUrl"]))

def search(query, start, num):
  query = urllib.parse.urlencode({"q" : query, "start" : start, "num" : num})
  print("query = {0}".format(query))
  url = "http://scholar.google.com/scholar?{0}".format(query)
  print("url = {0}".format(url))
  
  google_id = hashlib.md5(str(random.random()).encode()).hexdigest()[:16]  
  headers = [("User-Agent", "Mozilla/5.0"),("Cookie", "GSP=ID={0}:CF=4".format(google_id))]
  
  opener = urllib.request.build_opener()
  opener.addheaders = headers
  urllib.request.install_opener(opener)
  
  page = urllib.request.urlopen(url)
  
  print(page)  
  
  with open("page.html", "w") as f:
    f.write(page.read().decode("windows-1251"))
  


s = "Cited by 1 sdfsdfh Cited by 2 Cited by 3"
rePage = re.compile(r"Cited by (?P<num>[\d]+)")

li = map(lambda m: int(m.group("num")), rePage.finditer(s))
a = []
print(a)
a.extend(list(li))
print(a)

