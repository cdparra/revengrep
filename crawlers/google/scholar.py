# Helper library for work with Google

import urllib.request
import urllib.parse
import hashlib
import random

# helper type for working with Google Scholar Engine
class Engine:

  def __init__(self, perPage=10, pageNum=10):    
    self.__perPage = perPage
    self.__pageNum = pageNum    
    self.__curPage = 0
    
    google_id = hashlib.md5(str(random.random()).encode()).hexdigest()[:16]
    headers = [("User-Agent", "Mozilla/5.0"),("Cookie", "GSP=ID={0}:CF=4".format(google_id))]
    
    opener = urllib.request.build_opener()
    opener.addheaders = headers
    urllib.request.install_opener(opener)
    
        
  @property
  def query(self):
    return self.__query   
    
  @property
  def perPage(self):
    return self.__perPage
   
  @property
  def pageNum(self):
    return self.__pageNum  
    
  def search(self, query):
    self.__query = query
    self.__curPage = 0
    
  def __iter__(self):
    return self
   
  def __next__(self):
    if self.__curPage == self.__pageNum:
      raise StopIteration 
      
    # encode query
    start = self.__curPage * self.__perPage
    query = urllib.parse.urlencode({"q":self.__query, "start":start, "num":self.__perPage})
    url = "http://scholar.google.com/scholar?{0}".format(query)      
    self.__curPage += 1
      
    # open url
    page = urllib.request.urlopen(url)
    # decode page's content and return result
#    return page.read().decode("windows-1251")
    return page.read().decode("utf-8")
      
  def __str__(self):
    return ('Google Scholar Engine : '
    'perPage=[{0.perPage}] pageNum=[{0.pageNum}]'
    .format(self))
      
# class Engine
