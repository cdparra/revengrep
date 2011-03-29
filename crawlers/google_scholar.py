#!/usr/bin/python3.1

"""
A crawler for Google Scholar engine. Extrats infromation
over the Internet and calcualte differents metrics

Author: Denis Yarets (yaretsd@gmail.com)
Date: 27.03.2011
Project: revengrep
Python3.1
"""

import sys
import google.scholar
import re
import os
import scientist
    
    
def processFile(fileName, engine):
  res = []
  with open(fileName, "r") as f:
    for line in f:
      name = line.strip()
      print("\tauthor {0} is processed now...".format(name))
      author = scientist.Scientist(name)
      author.parseEngine(engine)
      res.append(author)
  return res      

def main():

  inputDir = sys.argv[1]
  outputDir = sys.argv[2]
  perPage = int(sys.argv[3]) if len(sys.argv) >= 4 else 10
  numPages = int(sys.argv[4]) if len(sys.argv) >= 5 else 10
  
  engine = google.scholar.Engine(perPage, numPages)
  
  for fname in os.listdir(inputDir):
    fullName = os.path.join(inputDir, fname)
    print("file {0} is processed now...".format(fname))
    if os.path.isfile(fullName):
      authors = processFile(fullName, engine)
      with open(os.path.join(outputDir, fname), "w") as f:
        for author in authors:
          f.write("{0}\n".format(author))      
  

def badArgs():
# not enough arguments are present
  print("Usage: {0} <input> <output> [<per_page>] [<num_pages>] [<params>]".format(__file__))
  sys.exit(1)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    badArgs()

  main()  
