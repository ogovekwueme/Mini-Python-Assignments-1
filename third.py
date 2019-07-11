#!/usr/bin/python3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print('The original list is',a)
new_a = [x for x in a if x < 5]
print('The new list with numbers less than 5 are',new_a)

#input from user

try:
    number = int(input('Enter a number from the list above:'))
except:
    print('Enter a valid integer')
else:
    if number not in a:
        print('Your number isn\'t in the list')
    else:
        b = [x for x in a if x < number]
        print('The new list is ',b)
