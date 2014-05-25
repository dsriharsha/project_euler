'''
Created on May 23, 2014

@author: Harsha

Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


Answer:
31875000
'''
from math import sqrt
from fractions import gcd


def main():
    for a in range(1,1000):
        for b in range(a + 1, 1000 - a - 1):
            c = 1000 - a - b
            if c*c == a*a + b*b:
                print a*b*c
                return

'''
This method uses euclid formula for generating primitive pythogorean triplets. The other concept used is if (a.b,c) is pythagorean triplet, so is d * (a,b,c)
a= 2mnd; b= d(m^2 -n^2); c= d(m^2 + n^2)
a + b + c = s
2mnd + (m^2 -n^2)d + (m^2 + n^2)d = s
2dm(m+n) = s
find m and k = m+n subject to k being odd
'''
def usingFormulaForPythagoreanTriples():
    s = 1000 
    #a + b + c = s
    s2 = s / 2
    mlimit = int(sqrt(s2))
    for m in range(2, mlimit) :
        if s2 % m == 0 :
            sm = s2 / m
            while sm % 2 == 0 :
                sm /= 2
            if m % 2 == 1 :
                k = m + 2
            else :
                k = m + 1
            while k < 2*m and k <= sm :
                if sm % k == 0 and gcd(k,m) == 1 :
                    d = s2 / (k*m)
                    n = k - m
                    a = d * (m*m - n*n)
                    b = 2 * d * m * n
                    c = d * (m*m + n*n)
                    print a * b * c
                    return
                k += 2            
     
if __name__ == '__main__':
    main()
    usingFormulaForPythagoreanTriples()