#!/usr/bin/python

'''
This programs prints out the divisor of 
a particular input

input: int
output: list
'''

number = int(input('Enter a number:'))
divisors = [x for x in range(2,number) if number % x == 0]

print('Your list of divisors are ', divisors)
