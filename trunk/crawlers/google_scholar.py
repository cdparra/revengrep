#!/usr/bin/python3.1

import sys
import google.scholar
import re

# This is the first attempt to create a same kind of spider/crawler 
# for fetching useful information about specified scientist from
# Google Scholar system


def matchName(rname, qname):
# match a name that was found with the real name
  # TODO: add here some logic
  if rname == qname:
    return True
  return False
  
def parseName(name):
# transmit the input author name into the usable version
  # TODO: add here some logic
  return name.replace("_", " ") 


def hIndex(cit):
# h-index
# A scientist has index h if h of [his/her] Np papers have at least h citations
# each, and the other (Np − h) papers have at most h citations each.
  for i in range(0, len(cit)):
    if i+1 > cit[i]:
      return i
  return len(cit)   
    
def gIndex(cit):
# g-index
# Given a set of articles ranked in decreasing order of the number of citations
# that they received, the g-index is the (unique) largest number such that
# the top g articles received (together) at least g^2 citations.     
  s = 0
  for i in range(0, len(cit)):
    s += cit[i]
    if s < i*i:
      return i
  return len(cit)  
    
          

def getCitationList(name, perPage, numPages):
  engine = google.scholar.Engine(name, perPage, numPages)
  
  print(engine)
  
  cit = []  
  citre = re.compile(r"Cited by (?P<cit>[\d]+)");
    
  for page in engine:
    ma = map(lambda m: int(m.group("cit")), citre.finditer(page))
    cit.extend(list(ma))

  cit.sort()
  cit.reverse()
  
  print("num_cit = {0}".format(len(cit)))
#  print("cit = {0}".format(cit))
  
  return cit   
    


def main():
  fin = sys.argv[1]
  fout = sys.argv[2]
  perPage = int(sys.argv[3]) if len(sys.argv) >= 4 else 10
  numPages = int(sys.argv[4]) if len(sys.argv) >= 5 else 10
  
  res = []
  with open(fin, "r") as f:
    for line in f:
      srh, name = line.strip().split(" ")
      rh = int(srh)
      print("{0} is processed...".format(name.replace("_", " ")))
      cit = getCitationList(parseName(name), perPage, numPages)
      h = hIndex(cit)
      dif = abs(rh - h)
      print("processing is ready, rh = {0:3d} h = {1:3d} dif = {2}"
      .format(rh, h, dif))
      res.append((rh, h, name, dif))
      
  sDif = 0    
  with open(fout, "w") as f:
    for rh, h, name, dif in res:
      sDif += dif
      f.write("rh = {0:3d} h = {1:3d} dif = {2:2d}  {3}\n".format(rh, h, dif, name))
    f.write("average dif = {0:.5f}\n".format(sDif / len(res)))  
 
  

def badArgs():
# not enough arguments are present
  print("Usage: {0} <input> <output> [<per_page>] [<num_pages>] [<params>]".format(__file__))
  sys.exit(1)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    badArgs()

  main()
  
