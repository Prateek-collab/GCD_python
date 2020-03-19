"""
A GCD function using Python
(The Naive Approach)
"""

def gcd (m,n):                  #GCD function
                fm=[]              #list1
                for i in range(1,m+1):
                                if (m%i==0):
                                                fm.append(i)
                fn=[]                #list2
                for j in range (1,n+1):
                                if(n%j==0):
                                                fn.append(i)
                cf=[]             #common factors
                for f in fm:
                                if f in fn:
                                                cf.append(f)
                return(cf[-1])                  #Largest or rightmost factor
