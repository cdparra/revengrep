
"""
Helper library for searching, keeping and calculating different metrics
for scientists.

Author: Denis Yarets (yaretsd@gmail.com)
Date: 27.03.2011
Project: revengrep
Python3.1
"""
import sys
import google.scholar
import re
import math

def parseName(name):
  return name.replace("_", " ").lower()

class Scientist:
  """
  This class represents a scientist. Can perform searhing over the Internet,
  calculate different metrics (f.e. h-index, g-index, etc.).
  
  You can find a description of the metrics here:
  http://www.liquidpub.org/mediawiki/index.php/Individual_authors_evaluation
  """ 

  def __init__(self, name):
    self.__name = name
    self.__cit = []    
    
  def parseEngine(self, engine):
    """
    Performs searching over the Internet via Google Scholar engine.
    From found atricles, papers, etc. tries to fetch a number of citation.
    """
    
    citre = re.compile(r"Cited by (?P<cit>[\d]+)");
        
    engine.search(self.name)    
    for page in engine:
      ma = map(lambda m: int(m.group("cit")), citre.finditer(page))
      self.cit.extend(list(ma))

    self.cit.sort()
    self.cit.reverse()  
    
  @property
  def name(self):
    return self.__name 
    
  @property
  def cit(self):
    return self.__cit  
    
  def citationCount(self):
    """
    Total number of citation.
    """
    return sum(self.cit)
    
  def averageCitation(self):
    """
    Average number of citation.
    """  
    if len(self.cit) == 0 : return 0.0
    return sum(self.cit) / len(self.cit)
    
  def hIndex(self):
    """
    A scientist has index h if h of his or her Np papers have
    at least h citations each and the other (Np − h) papers have fewer
    than h citations each (Hirsch, 2005).
    """
    for i in range(0, len(self.cit)):
      if i+1 > self.cit[i]: return i
    return len(self.cit)  

  def gIndex(self):  
    """
    The highest number g of papers that together received g2 or more
    citations (Egghe, 2006).
    """
    s = 0
    for i in range(0, len(self.cit)):
      s += self.cit[i]
      if (i+1)*(i+1) > s: return i
    return len(self.cit) 
    
  def mQuotient(self):
     """
     The ration h/y, where h = h index, y = number of years since publishing
     the first paper
     """
     raise Exception 
    
  def h2Index(self):
    """
    A scientist's h(2) index is defined as the highest natural number
    such that his h(2) most-cited papers received at least [h(2)2]
    citations (Kosmulski, 2006).
    """
    for i in range(0, len(self.cit)):
      if (i+1)*(i+1) > self.cit[i]: return i
    return len(self.cit)      
   
  def aIndex(self):
    """
    The A-index is the average number of citations of the papers in the
    h-core.
    """
    h = self.hIndex() 
    if h == 0: return 0
    return sum(self.cit[:h]) / h
    
  def mIndex(self):
    """
    The median number of citations received by papers in the Hirsch core
    (this is the papers ranking smaller than or equal to h).
    """
    h = self.hIndex()
    if h == 0: return 0
    return self.cit[h//2]
    
  def rIndex(self):
    """
    The R-index is the square root of citation of the papers in the h-core.
    """
    h = self.hIndex()
    if h == 0: return 0.0
    return math.sqrt(sum(self.cit[:h])) 
  
  def arIndex(self):
    """
    The square root of sum over all ratious of c/y, where c - number
    of citation, y - years since publishing.
    """
    raise Exception
    
  def calcMetrics(self):
    return {
    "cc" : self.citationCount(),
    "ac" : self.averageCitation(),
    "h-index" : self.hIndex(),
    "g-index" : self.gIndex(),
    "h2-index" : self.h2Index(),
    "a-index" : self.aIndex(),
    "m-index" : self.mIndex(),
    "r-index" : self.rIndex()
    }      
     
  def __str__(self):
    return "{0}\n{1}\n".format(self.name, self.calcMetrics())      

      
