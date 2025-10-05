import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) 

import os
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
#print(f'Welcome {sys.argv[1]}. Enjoy  {sys.argv[2]} challenge!')

# To know the largest integer variable it takes
print(sys.maxsize)
# To know environment path
print(sys.path)
# To know the version of python you are using
print(sys.version)

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       
print(median(ages))     
print(mode(ages))       
print(stdev(ages))  

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~

from random import *
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

#---------------------------------------------------------------------------------
#* Level 1 
print(50 * '-')
#Ex 1
def random_user_id(): 
    to_make = string.ascii_letters + string.digits
    id = ''
    for iter in range(8):
        id += choice(to_make)
    return f'Your password is : {id}'
print(random_user_id())

#Ex 2
def user_id_gen_by_user(): 
    num_of_chars = input("Input How many characters your password should have: ")
    num_of_IDs = input("Input How many IDs you want: ")
    to_make = string.ascii_letters + string.digits
    for passwords in range(int(num_of_IDs)):
        id = ''
        for iter in range(int(num_of_chars)):
            id += choice(to_make)

        print(id)
#print(user_id_gen_by_user())

#Ex 3
def rgb_color_gen():
    rgb = []
    for iter in range(3):
        rgb.append(randint(000,255))
    return f'RGB{rgb}'
print(rgb_color_gen())

#* Level 2
#Ex 1
def list_of_hexa_colors(how_many_colors):
    to_make = 'ABCDEF' + string.digits
    hexa = []
    for iter in range(how_many_colors):
        iterated_color = ''
        for number in range(6):
            iterated_color += choice(to_make)
        hexa.append(f'#{iterated_color}')
    return hexa
print(list_of_hexa_colors(3))

#Ex 2
def list_of_rgb_colors(how_many_colors):
    rgb = []
    for iter in range(how_many_colors):
        iterated_color = []
        for iter in range(3):
            iterated_color.append(randint(000,255))
        rgb.append(f'rgb{iterated_color}')
    return rgb
print(list_of_rgb_colors(2))

#Ex 3
def generate_colors(h_or_rgb,how_many_colors):
    if h_or_rgb == 'rgb':
        return list_of_rgb_colors(how_many_colors)
    else:
        return list_of_hexa_colors(how_many_colors)
print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors('hexa', 1)) # ['#b334ef']
print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
print(generate_colors('rgb', 1))  # ['rgb(33,79, 176)']