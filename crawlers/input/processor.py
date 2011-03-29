#!/usr/bin/python3.1

import sys
import os
import re

def lines(fileName):
  with open(fileName, "r") as f:
    for s in f:
      yield s.strip().replace(".", "")

if len(sys.argv) < 2:
  print("not enough params")
  sys.exit(0)
  
inputDir = sys.argv[1]
outputDir = sys.argv[2]

pat = re.compile(r"(?P<name>[\w -]+),[\w\(\), -]+\$")  

for name in os.listdir(inputDir):
  fullName = os.path.join(inputDir, name)
  print(fullName)
  if os.path.isfile(fullName):
    s = "$".join(lines(fullName))+"$"
    outName = name.replace("csv", "txt")
    with open(os.path.join(outputDir, outName), "w") as f:
      for match in pat.finditer(s):
        author = match.group("name").lower().replace("dr", "").replace("prof", "").replace("sir", "")
        f.write("{0}\n".format(author.strip().replace(" ", "_")))       
  







