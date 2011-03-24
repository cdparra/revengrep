#!/usr/bin/python3.1

import re
import sys

def lines(fileName):
  with open(fileName, "r") as f:
    for s in f:
      yield s.strip()

if len(sys.argv) < 2: 
  print("not enought params")
  sys.exit(1)
  
inputFile = sys.argv[1]
outputFile = sys.argv[2]  
  
pat = re.compile(r"(?P<hindex>[\d]+)[ \t]+(?P<name>[\w ]+)\(")  

s = " ".join(lines(inputFile))

with open(outputFile, "w") as f:
  for match in pat.finditer(s):
    f.write("{0} {1}\n".format(match.group("hindex"), match.group("name").strip().replace(" ", "_"))  )


  
  
