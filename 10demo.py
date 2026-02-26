# 10demo.py by sydney_haubursin
print('hello, again') # greeting

print(1.5e-2)
print(1 + 1) # addition
print(2 - 1) # subtraction
print(1 / 2) # division 
print(1 ** 2) # exponents
print(4 // 2 ) # interger_divide
print(5 % 2) # remainder
print(5 * (2 + 1)) # pemdas

print(abs(5)) # absolute_value
print(pow(3, 2)) # x_to_the_power_of_y
print(round(10, ndigits=3)) # roundoff_x_to_3_digits

import math
print(math.ceil(2.5)) # roundxup
print(math.floor(2.5)) # rounddown
print(math.log(2)) # x_in_log_base_e
print(math.sqrt(4)) # squareroot

print(0.1 * 1)
print(0.1 * 3)

a = 3                       # side of triangle
b = 4                       # side of triangle
c = math.sqrt(a**2 + b**2)  # hypotenuse 
print(c)
print(type (a), type(b), type(c), sep=', ', end='!\n')

def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))

