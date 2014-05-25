'''
Created on May 25, 2014

@author: Harsha

Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.


Answer:
142913828922
'''


def solve():
    limit = 2000000
    not_prime = set()
    _sum = 0
    for i in xrange(2,limit):
        if i in not_prime:
            not_prime.remove(i)
            continue
        for j in xrange(2*i, limit, i):
            not_prime.add(j)
        _sum += i    
    print _sum    



if __name__ == '__main__':
    solve()