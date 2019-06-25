# using python2
from datetime import date

curr_year = date.today().year

name = raw_input('Enter your name:')
age = int(raw_input('Enter your age:'))
age_diff = 100 - age
output = 'Hello %s, you will be 100 years old in year %d' % (name, curr_year+age_diff)
print(output)

n = int(raw_input('Enter a number:'))
for i in range(n):
    print(output)
