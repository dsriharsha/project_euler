'''
Created on May 23, 2014

@author: Harsha

Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


Answer:
6857
'''
from math import sqrt

if __name__ == '__main__':
    number = 600851475143 
    largest_prime_factor = current_factor = 2
    #A number can have atmost one prime factor greater than sqrt(number)
    max_factor = int(sqrt(number))
    while number > 1 and current_factor <= max_factor:
        if number % current_factor == 0 :
            largest_prime_factor = current_factor
            while number % current_factor == 0 :
                number /= current_factor
            max_factor = int(sqrt(number))
        current_factor += 1
    if number == 1 :
        print largest_prime_factor
    else :
        print number        
