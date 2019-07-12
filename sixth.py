#!/usr/bin/python3

s = input('Enter a word:')

if s[:] == s[::-1]:
    print('This word is a palindrome!')
else:
    print('This word is not a palindrome!!!')
