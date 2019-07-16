#!/usr/bin/python3

from random import  randint


guess = randint(1,9)
choice = int(input('Enter a number ranging from 1 to 9:'))
if choice == guess:
    print('It is a tie!')
elif choice < guess:
    print('Your choice is too low')
else:
    print('Your number is too high')
