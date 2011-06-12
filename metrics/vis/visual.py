#!/usr/bin/python3.1

import sys
import os

def getSizes(folder):
  sizes = []
  for name in sorted(os.listdir(folder)):
    if name.startswith("."): continue
    path = os.path.join(folder, name)
    with open(path, "r") as fin:
      sz = len(fin.readline().strip()[1:-1].split(","))
      sizes.append(sz)
  return sizes       
    
def getNames(fileName):
  names = []
  with open(fileName, "r") as fin:
    for line in fin:
      names.append(line.strip())
  return names  
  

def getCorrelation(folder):
  cor = []
  for name in sorted(os.listdir(folder)):
    if name.startswith("."): continue    
    path = os.path.join(folder, name)
    with open(path, "r") as fin:
      c = float(fin.readline().strip())
      cor.append(c)
  return cor

def main():
  names = getNames(sys.argv[1])
  sizes = getSizes(sys.argv[2])
  bfCor = getCorrelation(sys.argv[3])
  gaCor = getCorrelation(sys.argv[4])
  
  outFile = sys.argv[5]
  
  with open(outFile, "w") as fout:
    fout.write("= Results of Reverse Engineering =\n")     
    fout.write("|| *No* || *Department* || *No of Members* || *Brute Force* || *Genetic Algorithm* || *Improvement* ||\n")
    for i in range(0, len(names)):
      fout.write("|| {0:02d} ".format(i+1))
      fout.write("|| {0} ".format(names[i]))
      fout.write("|| {0} ".format(sizes[i]))
      fout.write("|| {0:5f} ".format(bfCor[i]))
      fout.write("|| {0:5f} ".format(gaCor[i]))                  
      diff = gaCor[i]-bfCor[i]
      if diff > 0.1:
        fout.write("|| *{0:5f}* ".format(diff))
      else:
        fout.write("|| {0:5f} ".format(diff))             
      fout.write("||\n")
  
  
def badArgs():
# not enough arguments are present
  print("Usage: {0} <names> <sizes> <bf_cor> <ga_cor> <output>".format(__file__))
  sys.exit(1)

if __name__ == "__main__":
  if len(sys.argv) < 6:
    badArgs()
  main()
    

