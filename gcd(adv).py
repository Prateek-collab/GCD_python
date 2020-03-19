"""
A GCD function using Python
(An Advanced Approach)
Since we all know the gcd of two numbers must not be greater than the minimum of two numbers.
So why to iterate on two lists, rather we can do it on one which is minimum amongst the two.
The elements common in both are added to the list 'cf'. The rightmost element is the GCD.
"""

def gcd (m,n):
                cf=[]   
                for i in range (1,min(m,n)+1):
                                if(m%i)==0 and (n%i)==0:
                                                cf.append(i)
                return(cf[-1])
