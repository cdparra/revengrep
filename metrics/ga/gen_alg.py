#!/usr/bin/python3.1

"""
A genetic algorithm for calculation the best approximation of the coefficients in a
linear combination of metrics to achieve the best correlation.

Author: Denis Yarets (yaretsd@gmail.com)
Date: 06.04.2011
Project: revengrep
Python3.1
"""

import sys
import math
import statistics
from functools import reduce
import random

dif = 0.2
eps = 1e-8
target_cor = 1.0
mutate_prob = 0.1
popul_size = 100
iter_num = 1000

def inputData(fileName):
  vctrs = []
  with open(fileName, "r") as fin:
    for line in fin:
      v = [float(x) for x in line.strip()[1:-1].split(",")]
      vctrs.append(v)
 
  return vctrs[0], vctrs[1:]
  
def normalize(m):
  mi, ma = min(m), max(m)
  return [1.0*(x-mi)/(ma-mi+1) for x in m]     
    
def getParent(fitneses):
  s = sum(fitneses)
  r = random.uniform(0, s)  
  parId = 0
  while r > 0:
    if r-fitneses[parId] < eps:
      return parId
    r -= fitneses[parId]
    parId += 1    
  return 0  

def crossover(x, y):
  bound = random.randint(0, len(x)-1)
  xy = [x[i] if random.random() < 0.5 else y[i] for i in range(0, len(x))]
  return xy

def mutation(x):
  nx = []
  for a in x:
    na = a
    if random.random() < mutate_prob:
      change = random.uniform(-0.2, 0.2)
      na += change
      if na < 0.0: na = 0.0
      if na > 1.0: na = 1.0
    nx.append(na)
  return nx 
  
def linearComb(a, x):
  empty = [0.0 for i in x[0]]   
  xa = [[x*a[i] for x in x[i]] for i in range(0, len(x))]      
  sm = reduce(lambda x, y: [x[i]+y[i] for i in range(0, len(x))], xa, empty)
  smn = normalize(list(sm))
  return smn
  
def calcFitness(genom, tar, vctrs):
  v = linearComb(genom, vctrs)
  cor = statistics.correlationPearson(v, tar)
#  cor = statistics.correlationKendallTau(v, tar)
  return abs(cor)
    
def geneticAlgorithm(tar, vctrs):
  population = []
  for i in range(0, popul_size):
    genom = [random.random() for x in vctrs]
    population.append(genom)
    
  bestFitness = -1e30
  bestGenom = []
  
  for it in range(0, iter_num):
    if it % 100 == 0:
      print("iteration {0}:".format(it))
      print("correlation = {0}".format(bestFitness))
      print("genom = {0}".format(["{0:.3f}".format(x) for x in bestGenom]))
      print("")
    fitneses = [calcFitness(genom, tar, vctrs) for genom in population]
    
    for i in range(0, len(population)):
      if fitneses[i] > bestFitness:
        bestFitness = fitneses[i]
        bestGenom = population[i]                
      
    generation = []
    for i in range(0, popul_size):
      xId = getParent(fitneses)   
      yId = getParent(fitneses)
       
      xy = crossover(population[xId], population[yId])
      xy = mutation(xy)
      generation.append(xy)       

    population = generation 
  
  return bestGenom   

def main():
  inFile = sys.argv[1]
  outFile = sys.argv[2]
  
  ranks, metrics = inputData(inFile)  
  
#  print("ranks: \n{0}".format(ranks))
#  print("metrics: \n{0}".format(metrics))
  
  genom = geneticAlgorithm(ranks, metrics)  
  
  with open(outFile, "w") as fout:
    cor = calcFitness(genom, ranks, metrics)
    print("processing is done!")
    print("correlation = {0}".format(cor))    
    print("genom = {0}".format(genom))    
    fout.write("{0:5f}\n{1}\n".format(cor, genom))
  
  

def badArgs():
# not enough arguments are present
  print("Usage: {0} <input> <output>".format(__file__))
  sys.exit(1)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    badArgs()
  main()
  
  
