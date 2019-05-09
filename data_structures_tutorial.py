#Data Structures for Python Tutorial with Jupyter Notebook
from math import sqrt

s = 'hello'
s.upper()
# To see a list of methods available, press tab after the . 

#Big O Notation
def sumToN(n):
  '''
  Take an input of n and return the sum of the numbers from 0 to n
  '''
  sum = 0
  for x in range(n+1):
    sum += x
  return sum

def sumToN2(n):
  return (n*(n+1))/2

