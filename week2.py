"""1.positive integer m is a prime product if it can be written as p×q, where p and q are both primes. .

Write a Python function primeproduct(m) that takes an integer m as input and returns True if m is a prime product and False otherwise. (If m is not positive, your function should return False.)

Here are some examples of how your function should work.

>>> primeproduct(6)
True

>>> primeproduct(188)
False

>>> primeproduct(202)
True

*********************************************************CODE****************************************************************************************************************************
"""
def checkprime(n):
    p=0
    for i in range (1,n+1):
        if n%i==0:
           p=p+1
    if p<=2 :
       return(True)
    else:
       return(False)



def primeproduct(m):
    if m<0:
        return(False)
    factors = []
    for i in range(1,m+1):
        if m%i ==0:
            factors.append(i)
    for i in factors:
      quotient = m//i
      if checkprime(quotient)==True and checkprime(i)==True:
         return(True) 
    return(False)
"""
*****************************************************************************************************************************************************************************************


2.Write a function delchar(s,c) that takes as input strings s and c, where c has length 1 (i.e., a single character), and returns the string obtained by deleting all occurrences of c in s. If c has length other than 1, the function should return s

Here are some examples to show how your function should work.

 
>>> delchar("banana","b")
'anana'

>>> delchar("banana","a")
'bnn'

>>> delchar("banana","n")
'baaa'

>>> delchar("banana","an")
'banana'

**************************************************************************CODE************************************************************************************************************
"""
def delchar(s,c):
  if len(c)>1:
    return(s)
  v=list(s)
  out=""
  for i in range(0,len(v)):
      if c!=v[i]:
        out=out+v[i]
  return(out)

"""""
*****************************************************************************************************************************************************************************************
3.Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, and returns a list consisting of the first element in l1, then the first element in l2, then the second element in l1, then the second element in l2, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.

Here are some examples to show how your function should work.

>>> shuffle([0,2,4],[1,3,5])
[0, 1, 2, 3, 4, 5]

>>> shuffle([0,2,4],[1])
[0, 1, 2, 4]

>>> shuffle([0],[1,3,5])
[0, 1, 3, 5]

***********************************************************************CODE*****************************************************************************************************************
"""
def shuffle(l1,l2):
    c=[]
    if len(l1)!=0 and len(l2)!=0:
      for i in range(min(len(l1), len(l2))):
        c.extend([l1[i],l2[i]])      
      c.extend(l1[i+1:] or l2[i+1:])
    else:
      c.extend(l1[0:] or l2[0:])      
    return (c)