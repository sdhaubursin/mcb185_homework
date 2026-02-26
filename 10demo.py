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

def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h
def triangle_area(w, h): return rectangle_area(w, h) / 2

def farenheit_to_celsius(f): return (f - 32) * 5/9
print(farenheit_to_celsius(68))

def mph_to_kph(m): return m * 1.60934
print(mph_to_kph(10))

s = 'hello world'
print(s, type(s))

a = 2
b = 3 
if a != b:
	print('a not equal to b')
print(a , b)

def is_even(x):
	if x % 2 == 0: return True
	return False 
print(is_even(2))
print(is_even(3))

c = a == b
print(c)
print(type(c))

if   a < b: print('a < b')
elif a > b: print('a > b')

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b print('you are living in a strange world')
if not False: print(True)

print(abs(a - b))
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')