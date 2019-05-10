# Data Structures for Python Tutorial with Jupyter Notebook
from math import sqrt

s = 'hello'
s.upper()
# To see a list of methods available, press tab after the . 

#Big O Notation - Describes how quickly runtime will grow relative to the size of the input
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

# O(1) - Constant
# log(n) - Logarithmic
# O(n) - Linear

# O(1)
def func_constant(values):
  print values[0]

func_constant([1,2,3])
# 1

# O(n)
def func_lin(lst):
  for val in lst:
    print val
