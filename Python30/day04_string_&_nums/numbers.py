x = 5
y = 5.7
z = 2 + 3j


print(type(x))
print(type(y))
print(type(z))

print('-' * 30)

x = "24"
print(type(x))
x = int(x)
print(type(x))
print(x * 3)

print('-' * 30)

x = 3.14
print(int(x))

x = '3.14'
print(float(x))

x = 3
y = 4
print(complex(x,y))

print('-' * 30)
'''
Rounding
'''

print(abs(2-10))

import math

price = 35.53879865
print(round(price))
print(math.floor(price))
print(math.ceil(price))


import random

print(random.random())
print(random.randint(1, 10))


# Challange z odcinka Python Numbers Mastery od Data With Baara
print('-' * 30)

a = random.randint(1,100)
print(a)
if a % 2 == 0:
    print('Even')
else: 
    print('Odd')