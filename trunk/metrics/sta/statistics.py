
"""
Statistics support.

Author: Denis Yarets (yaretsd@gmail.com)
Date: 18.04.2011
Project: revengrep
Python3.1
"""
import math

  
def compareTo(a, b):
  """CompareTo method"""
  if a < b: return -1
  if a > b: return 1
  return 0    
  
def correlationKendallTau(x, y):
  """Kendall tau rank correlation coefficient."""
  px = [compareTo(x[i], x[j]) for i in range(0, len(x)) for j in range(0, i)]
  py = [compareTo(y[i], y[j]) for i in range(0, len(y)) for j in range(0, i)]
  numerator = sum([px[i]*py[i] for i in range(0, len(px))])
  n = len(x)
  res = 2.0*numerator/n/(n-1)
  return abs(res)
  
def meanValue(x):
  """Mean value for discrete uniform distibution."""
  x = list(x)
  return 1.0*sum(x)/len(x)  
  
def correlationPearson(x, y):
  """Pearson product-moment correlation coefficient."""
  mx, my = meanValue(x), meanValue(y)
  mx2, my2 = meanValue(map(lambda a, b: a*b, x, x)), meanValue(map(lambda a, b: a*b, y, y))
  mxy = meanValue(map(lambda a, b: a*b, x, y))
  if mx2-mx**2 == 0 or my2-my**2 == 0: return 0.0
  res = (mxy-mx*my)/(math.sqrt(mx2 - mx**2)*math.sqrt(my2-my**2))      
  return abs(res)
  
