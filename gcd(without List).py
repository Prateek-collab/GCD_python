"""
A GCD function using Python
(Without use of List Data Structure)
Since we all need only the highest common factor present. Instead of creating a list we can declare a variabe
that will be updated at each iteration and finally give us the highest common factor.
"""

def gcd (m,n):
                for i in range (1,min(m,n)+1):
                                if(m%i)==0 and (n%i)==0:
                                                mrcf=i                          #variable to be updated
                return(mrcf)
