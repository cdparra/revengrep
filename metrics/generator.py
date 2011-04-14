#!/usr/bin/python3.1

"""
Create random scientists with random metrics according to correlation.

Author: Denis Yarets (yaretsd@gmail.com)
Date: 10.04.2011
Project: revengrep
Python3.1
"""

import sys
import math
import re
import random

def getMetricsList(s):
  metre = re.compile(r"(?P<met>[\w_]+)")
  return list(map(lambda m: m.group("met"), metre.finditer(s)))

def extractCorrelation(fileName):
  corr = []
  with open(fileName, "r") as fin:
    for line in fin:
      crs, s = line.split(" ==> ")
#      print(crs, s)
      met = getMetricsList(s)
#      print(met)
      if len(met) == 1:
        corr.append((float(crs), met[0]))
  corr.sort()
  corr.reverse()
  return corr
  
def generateMetrics(total, rank, corr):
  return [str(random.randint(0, total-rank)) for i in corr]  

def main():
  inFile = sys.argv[1]
  outFile = sys.argv[2]
  numScnt = int(sys.argv[3])
  
  corr = extractCorrelation(inFile)
#  print(corr)
#  print(len(corr))

  with open(outFile, "w") as fout:
    fout.write("\"rank\",{0}\n".format(",".join(map(lambda x: "\""+x[1]+"\"", corr))))
    
    for i in range(1, numScnt+1):
      fout.write("{0},{1}\n".format(i, ",".join(generateMetrics(numScnt, i, corr))))
  
  

def badArgs():
# not enough arguments are present
  print("Usage: {0} <input> <output> <num_of_scientists>".format(__file__))
  sys.exit(1)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    badArgs();
  main()
