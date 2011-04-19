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
import statistics

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
  
  
def allSubsets(people, calcCorrelation):
  """Try all subsets and find the correlation."""
  ranks = extractMetric(people, "rank")
  result = []
  empty = [0.0 for x in range(0, len(people))];
  for mask in range(1, 1<<len(metrics)):
    metrcs = extractMetrics(people, mask)
    # find a mean vector
    sm = reduce(lambda x, y: [x[i]+y[i] for i in range(0, len(x))], metrcs, empty)
    snm = [x/len(metrcs) for x in sm]
    cor = calcCorrelation(ranks, snm)
    #print("{0} = {1:5f}".format(mask, cor))
    result.append((cor, mask))
  result.sort(key=lambda x: abs(x[0]));
  result.reverse()  
  return result    
  
def printResult(result, fileName):
  with open(fileName, "w") as fout:
    for x, mask in result:
      ms = filter(lambda i: (mask&(1<<i)), range(0, len(metrics)))
      sts = map(lambda i: metrics[i], ms)
      fout.write("{0:5f} ==> {1}\n".format(x, list(sts)))   
  
def calcPearson(people):
  print("Pearson's correlation:")
  result = allSubsets(people, statistics.correlationPearson)
  printResult(result, "pearson_corr.txt")
  
def calcKendall(people):
  print("Kendall's correlation:")
  result = allSubsets(people, statistics.correlationKendallTau)
  printResult(result, "kendall_corr.txt")    
 
def extractSections(people):
  sections = [d.get("section") for d in people]
  return sorted(list(set(sections))) 
 
def printResultBySections(result, fileName):
  with open(fileName, "w") as fout:
    for sec, subresult in sorted(result.items()):
      fout.write("section {0}\n".format(sec))
      for x, mask in subresult:
        ms = filter(lambda i: (mask&(1<<i)), range(0, len(metrics)))
        sts = map(lambda i: metrics[i], ms)
        fout.write("{0:5f} ==> {1}\n".format(x, list(sts)))      
     
  
def calcPearsonBySections(people):
  print("Pearson's correlation by sections:")
  sections = extractSections(people)
  
  result = {}
  for sec in sections:
    print("section {0}:".format(sec))
    subpeople = list(filter(lambda x: x.get("section") == sec, people))
    subresult = allSubsets(subpeople, statistics.correlationPearson)
    result[sec] = subresult[0:10]
  
  printResultBySections(result, "pearson_corr_by_sec.txt")
  
def calcKendallBySections(people):
  print("Kendal's correlation by sections:")
  sections = extractSections(people)
  
  result = {}
  for sec in sections:
    print("section {0}:".format(sec))
    subpeople = list(filter(lambda x: x.get("section") == sec, people))
    subresult = allSubsets(subpeople, statistics.correlationKendallTau)
    result[sec] = subresult[0:10]
  
  printResultBySections(result, "kendall_corr_by_sec.txt")  
    
      
def main():              
  inFile = sys.argv[1]    
  people = inputData(inFile)  
  
#  calcPearson(people)
#  calcKendall(people)
  calcPearsonBySections(people)
  calcKendallBySections(people)

def badArgs():
# not enough arguments are present
  print("Usage: {0} <input>".format(__file__))
  sys.exit(1)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    badArgs()
  main()
