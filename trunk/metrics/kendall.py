 
"""
Calculate Kendall correlation coefficients between two ranked 
vectors

Author: Cristhian Parra (cdparra@gmail.com)
Date: 13.04.2011
Project: revengrep

Adapted from http://adorio-research.org/wordpress/?p=10787
authored by
  Ernesto Adorio, Ph.D.
  UPDEPP (U.P. at Clarkfield)
"""
 
from math import sqrt
 
 
def countties(Xranks, issorted = True, ztol = 1.0e-5):
    """
    Returns an array of pairs (n, x) where n is the tied count and x is the
    tied value.
    """
    tiescount = []
    if not issorted:
        X = sorted(Xranks) 
    else:
        X = Xranks
    x      = X[0]
    ncount = 1
    n      = len(X)
    for j in range(1, n):
      if abs(X[j] - x)< ztol:
         ncount += 1
      else:
        if ncount > 1:
           tiescount.append((ncount, x))
        ncount = 1
        x = X[j]
    # last pair value
    if ncount > 1:
       tiescount.append((ncount, x))
 
    return tiescount 
 
def kendall(X,Y, ztol = 1.0e-5):
    """
    Computes the Kendall tau correlation coefficient for input
    ordinal data X and Y.
    """
    n = len(X)
 
    xi = [(x,i) for i, x in enumerate(X)]
    xi.sort()
    yi = [Y[i] for (x,i) in xi]
    L, G = 0, 0
 
    # count ties.
    tx = countties(X, issorted=True)
    ty = countties(yi)
    Tx = sum([i*(i-1) for (i, x) in tx])*0.5
    Ty = sum([i*(i-1) for (i, x) in ty])*0.5
    for i in range(n):
        # Count number of < and > ranked data for the corresponding y elements.
        l, g = 0, 0
        ycmp = yi[i]
        for j in range(i+1, n):
            if  yi[j] > ycmp: 
               g += 1
            elif yi[j] < ycmp:
               l += 1
        L+= l
        G+= g
    f =  0.5 * n * (n-1)
    den = sqrt((f - Tx)* (f - Ty))
    tau = (G - L)/ den
    return L, G, tau
 
def test():
    """
    A test case from Dr. Flordeliza C. Reyes, "Applied Basic Statistics"
    """
    dataset = 2
 
    if dataset == 1: # without ties.
       X = range(1, 9)
       Y = [1, 4, 5,3,2,7,8,6]
    elif dataset == 2: # test for ties.
       X = [1,3,3,3,5,6,7.5, 7.5, 9, 10]
       Y = [1,2,3,5,6,4,9, 7.5, 7.5, 10] 
    return kendall(X,Y)
 
if __name__ == "__main__":
   print test()
