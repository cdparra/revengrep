#!/usr/bin/python3.1

"""
A helper for extracting the metrics from the input file and spliting
them by sections.

Author: Denis Yarets (yaretsd@gmail.com)
Date: 07.04.2011
Project: revengrep
Python3.1
"""

import sys
import os
import math
from functools import reduce

metrics = ("rank", "gs_pub", "gs_citedpub", "gs_citations", "gs_hindex", "gs_gindex", "gs_aindex", "gs_h2index", "gs_eindex")


def inputData(fileName):  
  """Reads the data from the input file."""  
  people = []
  keys = None
    
  with open(fileName, "r") as fin:
    for line in fin:
      if keys is None:
        keys = list(map(lambda s: s[1:-1].lower(), line.strip().split(",")))
      else:         
        vals = [s[1:-1] if s.startswith("\"") else s for s in line.strip().split(",")]
        people.append(dict(zip(keys, vals)))
        
  return people 
  
def extractSections(people):
  sections = [d.get("section") for d in people]
  return sorted(list(set(sections)))   

def normalizeMetric(m):
  """Normalize the input vector. Now all element will be in range [0,1]."""  
  mi, ma = min(m), max(m)
  return [1.0*(x-mi)/(ma-mi+1) for x in m]  
  
def extractMetric(people, key):
  """Extract a vector for particular metric."""    
  m = [float(d.get(key)) for d in people]
  return normalizeMetric(m)   

  
def main():              
  inFile = sys.argv[1] 
  outFolder = sys.argv[2]   
  people = inputData(inFile)  
  
  sections = extractSections(people)
  
  if not os.path.exists(outFolder):
    os.mkdir(outFolder)
  
  for sec in sections:
    print("section {0}:".format(sec))
    
    subpeople = list(filter(lambda x: x.get("section") == sec, people))
    print("\tnumber of entries: {0}".format(len(subpeople)))
      
    outFile = os.path.join(outFolder, "section{0}.txt".format(sec))        
    
    with open(outFile, "w") as fout:
      for key in metrics:
        vect = extractMetric(subpeople, key)
        fout.write("{0}\n".format(vect)) 


def badArgs():
# not enough arguments are present
  print("Usage: {0} <input-file> <output-folder".format(__file__))
  sys.exit(1)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    badArgs()
  main()  
        
