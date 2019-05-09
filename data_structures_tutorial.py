#Data Structures for Python Tutorial with Jupyter Notebook
from math import sqrt

s = 'hello'
s.upper()
# To see a list of methods available, press tab after the . 

#Big O Notation
def sumToN(n):
  sum = 0
  for x in range(0, n+1):
    sum += x
  return sum

def sumToN2(n):
  return (n*(n+1))/2
