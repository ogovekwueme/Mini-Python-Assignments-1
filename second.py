n = int(raw_input('Enter a number:'))
if n % 2 == 0:
    print('Your number is even')
else:
    print('Your number is odd')

if n % 4 == 0: print('Your number is even and divisible by 4')

quotient = int(raw_input('Enter a quotient (numerator):'))
divisor = int(raw_input('Enter divisor (denominator):'))
if quotient % divisor == 0:
    print('Your quotient is a multiple of the divisor')

