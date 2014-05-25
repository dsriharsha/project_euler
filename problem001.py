'''
Created on May 22, 2014

@author: Harsha


Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.


Answer:
233168
'''

if __name__ == '__main__':
    multiples_of_3 = int(999 / 3);
    multiples_of_5 = int(999 / 5);
    multiples_of_15 = int(999 / 15);
    value = 3 * (multiples_of_3 * (multiples_of_3 + 1)) / 2 + 5 * (multiples_of_5 * (multiples_of_5 + 1)) / 2 - 15 * (multiples_of_15 * (multiples_of_15 + 1)) / 2
    print value