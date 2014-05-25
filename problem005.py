'''
Created on May 23, 2014

@author: Harsha

Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


Answer:
232792560
'''
from math import log

if __name__ == '__main__':
    number = 20
    prime_multipliers = []
    not_prime = set()
    for i in range(2,number+1):
        if i in not_prime:
            continue
        for j in range(2*i, number+1, i):
            not_prime.add(j)
        max_power = int(log(number, i))
        prime_multipliers.append(pow(i, max_power))    
    lcm = 1
    for x in prime_multipliers : lcm *= x
    print lcm    