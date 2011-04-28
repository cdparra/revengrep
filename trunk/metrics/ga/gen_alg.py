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
popul_size = 20

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
#  print("crossover")
#  print("x : {0}".format(x))
#  print("y : {0}".format(y))  
  bound = random.randint(0, len(x)-1)
  xy = [x[i] if random.random() < 0.5 else y[i] for i in range(0, len(x))]
#  xy = [x[i] if i < bound else y[i] for i in range(0, len(x))]
#  print("xy : {0}".format(xy))  
  return xy

def mutation(x):
  for a in x:
    if random.random() < mutate_prob:
      change = random.uniform(-0.1, 0.1)
      a += change
      if a < 0.0: a = 0.0
      if a > 1.0: a = 1.0
  return x 
  
def linearComb(a, x):
  empty = [0.0 for i in x[0]]
#  print("linearComb");
#  print("genom : {0}".format(a))
#  print("x before : {0}".format(x[0][:5]))
   
   
  xa = [[x*a[i] for x in x[i]] for i in range(0, len(x))] 
   
#  for i in range(0, len(x)):
#    for j in range(0, len(x[i])):
#      x[i][j] *= a[i]
#  print("x after : {0}".format(xa[0][:5])) 
#  sys.exit(0)
     
  sm = reduce(lambda x, y: [x[i]+y[i] for i in range(0, len(x))], xa, empty)
  smn = normalize(list(sm))
#  print("norm: {0}".format(smn[:5])) 
  return smn
  
def calcFitness(genom, tar, vctrs):
  v = linearComb(genom, vctrs)
  cor = statistics.correlationPearson(v, tar)
  return abs(cor)
    
def geneticAlgorithm(tar, vctrs):
  population = []
  for i in range(0, popul_size):
    genom = [random.random() for x in vctrs]
    population.append(genom)
    
  bestFitness = -1e30
  bestGenom = None  
  
  for it in range(0, 200):
#    print("ga iter {0}:", it)
    fitneses = [calcFitness(genom, tar, vctrs) for genom in population]
    for i in range(0, len(population)):
      if fitneses[i] > bestFitness:
        bestFitness = fitneses[i]
        bestGenom = population[i]                
#    print("bestFitness = {0:5f}".format(bestFitness))  
#    print("bestGenom = {0}".format(bestGenom[:3])) 
    #print("have to be = {0:5f}".format(calcFitness(bestGenom, tar, vctrs)))
#    print("top3 : {0}".format(sorted(fitneses, key=lambda x:-x)[:3]))
#    print("genom : {0}".format(population[0][:3]))
      
    generation = []
    for i in range(0, popul_size):
#      if i % 10 == 0:
#        print("\tgeneration : {0}\n".format(i))
      xId = getParent(fitneses)   
      yId = getParent(fitneses)
       
      xy = crossover(population[xId], population[yId])
      xy = mutation(xy)
      generation.append(xy)
       
#    print("gen: {0}".format(population[0][:5]))   
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
    print("correlation = {0:5f}".format(cor))
    print("genom = {0}".format(genom))
    fout.write("{0}\ncorrelation = {1:5f}\n".format(genom, cor))
  
  

def badArgs():
# not enough arguments are present
  print("Usage: {0} <input> <output>".format(__file__))
  sys.exit(1)

if __name__ == "__main__":
  if len(sys.argv) < 3:
    badArgs()
  main()
  
  
