#!/usr/bin/python3.1

import sys

def inputData(fileName):  
  people = []
  keys = None
    
  with open(inFile, "r") as fin:
    for line in fin:
      if keys is None:
        keys = list(map(lambda s: s[1:-1], line.strip().split(",")))
      else:         
        vals = [s[1:-1] if s.startswith("\"") else s for s in line.strip().split(",")]
        people.append(dict(zip(keys, vals)))
        
  return people     
  
def extractVariable(a, key):
  return [d[key] for d in a]
  

def correlation(x, y):
  return 0.0  
      
def main():              
  inFile = sys.argv[1]
  xName = sys.argv[2]
  yName = sys.argv[3]
  
  people = inputData
  x = extractVariable(people, xName)
  y = extractVariable(people, yName)
  
  print(correlation(x, y))
  

def badArgs():
# not enough arguments are present
  print("Usage: {0} <input> <var1> <var2>".format(__file__))
  sys.exit(1)

if __name__ == "__main__":
  if len(sys.argv) < 4:
    badArgs()
  main()
