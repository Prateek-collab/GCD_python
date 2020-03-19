"""
A GCD function using Python
(Without use of List Data Structure)
Since we all need only the highest common factor present. A better approach would be to iterate fro the backward edge.
The first common factor encountered would give us the result.
"""

def gcd (m,n):
                i=min(m,n)
                while i>0:                      #opposite loop
                                if (m%i==0 and n%i==0):
                                                return(i)
                                else:
                                                i=i-1           #decrementer
