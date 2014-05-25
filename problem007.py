'''
Created on May 23, 2014

@author: Harsha

10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


Answer:
104743
'''

def main():
    number = 1000000
    not_prime = set()
    prime_count = 0
    for i in xrange(2,number):
        if i in not_prime:
            not_prime.remove(i)
            continue
        for j in xrange(2*i, number, i):
            not_prime.add(j)
        prime_count += 1    
        if prime_count == 10001:
            print i
            return
    print prime_count    

if __name__ == '__main__':
    main()