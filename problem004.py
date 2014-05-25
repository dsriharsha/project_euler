'''
Created on May 23, 2014

@author: Harsha

Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Answer:
906609
'''


def isPalindrome(num):
    numString = str(num)
    length = len(numString)
    for index in range(length/2) :
        if numString[index] != numString[length-1-index] :
            return False
    return True    

def main():
    largest_palindrome = 1
    num1 = 999
    while num1 >= 100:
        num2 = num1
        while num2 >= 100:
            num = num1 * num2
            if isPalindrome(num) :
                if num > largest_palindrome:
                    largest_palindrome = num
            num2 -= 1
        num1 -= 1            
    print largest_palindrome                

if __name__ == '__main__':
    main()
    
'''
alternate : slightly faster
The palindrome can be written as:

abccba

Which then simpifies to:

100000a + 10000b + 1000c + 100c + 10b + a

And then:

100001a + 10010b + 1100c

Factoring out 11, you get:

11(9091a + 910b + 100c)

So the palindrome must be divisible by 11.  Seeing as 11 is prime, at least one of the numbers must be divisible by 11.


'''    
