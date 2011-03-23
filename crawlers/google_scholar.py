#!/usr/bin/python3.1
import sys

# This is the first attempt to create a some kind of spider/crawler 
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
  return name  



def main():
  rname = parseName(sys.argv[1])
  
  
  

def badArgs():
# not enough arguments are present
  print("Usage: {0} <author_name> [<params>]".format(__file__))
  sys.exit(1)

if __name__ == "__main__":
  if len(sys.argv) < 2:
    badArgs()

  main()
  
