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

def inputData(fileName):
  vctrs = []
  with open(fileName, "r") as fin:
    for line in fin:
      v = [float(x) for x in line.strip()[1:-1].split(",")]
      vctrs.append(v)
 
  return vctrs[0], vctrs[1:]    

def extractVectors(vctrs, mask):
  """Extract vectors for particular mask."""
  ms = filter(lambda i: (mask&(1<<i)), range(0, len(vctrs)))
  return [vctrs[i] for i in ms]    
  
def bruteForceAlgorithm(tar, vctrs):
  """Try all subsets and find the correlation."""
  
  bestCor = -1e30
  bestMask = []
  
  empty = [0.0 for x in range(0, len(tar))];
  tot = 1<<len(vctrs)
  for mask in range(tot-1, tot):
    subv = extractVectors(vctrs, mask)
    
    sm = reduce(lambda x, y: [x[i]+y[i] for i in range(0, len(x))], subv, empty)
    smn = [x/len(subv) for x in sm]
    
    cor = statistics.correlationPearson(smn, tar)
    
    if cor > bestCor:
      bestCor = cor
      bestMask = [int(1 if mask&(1<<i) else 0) for i in range(0, len(vctrs))]
      
  return bestCor, bestMask
      
def main():              
  inFile = sys.argv[1]    
  outFile = sys.argv[2]
  
  ranks, metrics = inputData(inFile)  
  
  cor, vctr = bruteForceAlgorithm(ranks, metrics)
  
  with open(outFile, "w") as fout:
    print("processing is done!")
    print("correlation = {0}".format(cor))    
    print("vector = {0}".format(vctr))    
    fout.write("{0:5f}\n{1}\n".format(cor, vctr)) 


def badArgs():
# not enough arguments are present
  print("Usage: {0} <input> <output>".format(__file__))
  sys.exit(1)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    badArgs()
  main()
