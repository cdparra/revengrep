#!/usr/bin/python3.1

"""
A script for calculation the relation between scientists' rank 
and other metrics which are present in CNRS data.

First attempt is to find the correlation between rank and every
subset of metrics.

Author: Denis Yarets (yaretsd@gmail.com)
Date: 04.04.2011
Project: revengrep
Python3.1
"""

import sys
import math
from functools import reduce

metrics = ("gs_pub", "gs_citedpub", "gs_citations", "gs_hindex", "gs_gindex", "gs_aindex", "gs_h2index", "gs_eindex")

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
        
#  print(people)      
  return people     

def normalizeMetric(m):
  """Normalize the input vector. Now all element will be in range [0,1]."""  
  mi, ma = min(m), max(m)
  return [1.0*(x-mi)/(ma-mi+1) for x in m]  
  
def extractMetric(people, key):
  """Extract a vector for particular metric."""    
  m = [float(d.get(key)) for d in people]
  return normalizeMetric(m)  
  
def extractMetrics(people, mask):
  """Extract vectors for particular mask."""
  ms = filter(lambda i: (mask&(1<<i)), range(0, len(metrics)))    
  return list(map(lambda i: extractMetric(people, metrics[i]), ms))    
  
def mean(x):
  """Mean value."""
  y = list(x)
  return 1.0*sum(y)/len(y)  
  
def correlation(x, y):
  """Calc the correlation between x and y."""
  mx, my = mean(x), mean(y)
  mx2, my2 = mean(map(lambda a, b: a*b, x, x)), mean(map(lambda a, b: a*b, y, y))
  mxy = mean(map(lambda a, b: a*b, x, y))
  return (mxy-mx*my)/(math.sqrt(mx2 - mx**2)*math.sqrt(my2-my**2))    
  
def allSubsets(people):
  """Try all subsets and find the correlation."""
  ranks = extractMetric(people, "rank")
  result = []
  empty = [0.0 for x in range(0, len(people))];
  for mask in range(1, 1<<len(metrics)):
    metrcs = extractMetrics(people, mask)
    # find a mean vector
    sm = reduce(lambda x, y: [x[i]+y[i] for i in range(0, len(x))], metrcs, empty)
    snm = [x/len(metrcs) for x in sm]
    cor = correlation(ranks, snm)
    print("{0} = {1:5f}".format(mask, cor))
    result.append((cor, mask))
  result.sort();
  result.reverse()  
  return result    
      
def main():              
  inFile = sys.argv[1]
  outFile = sys.argv[2]
  
  people = inputData(inFile)
  result = allSubsets(people)

  with open(outFile, "w") as fout:
    for x, mask in result:
      ms = filter(lambda i: (mask&(1<<i)), range(0, len(metrics)))
      sts = map(lambda i: metrics[i], ms)
      fout.write("{0:5f} ==> {1}\n".format(x, list(sts)))  

def badArgs():
# not enough arguments are present
  print("Usage: {0} <input> <output>".format(__file__))
  sys.exit(1)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    badArgs()
  main()