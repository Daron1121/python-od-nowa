
#! Function as a Parameter

def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

#! Function as a Return Value

def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

#! Python Closure

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

#! Python Decorators

# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

#! Accepting Parameters in Decorator Functions

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

#! Python - Map Function

numbers = [1, 2, 3, 4, 5] # iterable
numbers_squared = map(lambda x : x**2, numbers)
print(list(numbers_squared))

#! Python - Filter Function

# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

#! Python - Reduce Function
from functools import *
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15

print(50 * '-')
#------------------------------------------------------
#* Exercises
#------------------------------------------------------
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Nepal']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#* Lvl 1
#Ex 1 Explain the difference between map, filter, and reduce.
'''
map - it change every iterable by called function 
filter - it returns only values that check condition in function
reduct - it returns a single value that represent the output of function in iterable
'''
#Ex 2 Explain the difference between higher order function, closure and decorator
'''
higher order function - its a function that have as a argument other smaller order function np small def or lambda
closure - it is defining function in other function(nesting)
decorator - its a of using function into other funct using @name_of_higer_order_funct before declaring another funct((poprawna definicja) This decorator function is a higher order function that takes a function as a parameter )
'''
#Ex 3
def call(x):
    return x

print(call(countries))
#Ex 4
for country in countries:
    print(country)

#Ex 5
for name in names:
    print(name)

#Ex 6
for number in numbers:
    print(number)

#* Exercises: Level 2
#Ex1 Use map to create a new list by changing each country to uppercase in the countries list
print(list(map(lambda name : name.upper(), countries)))

#Ex2 Use map to create a new list by changing each number to its square in the numbers list
square_roots = list(map(lambda x : x**2, numbers))
print(square_roots)

#Ex3 Use map to change each name to uppercase in the names list
print(list(map(lambda name : name.upper(), names)))

#Ex4 Use filter to filter out countries containing 'land'.
land_countries = list(filter(lambda country : country.endswith('land'), countries))
print(land_countries)

#Ex5 Use filter to filter out countries having exactly six characters.
num_6_countries = list(filter(lambda country : len(country) == 6, countries))
print(num_6_countries)

#Ex6 Use filter to filter out countries containing six letters and more in the country list.
num_6_or_more_countries = list(filter(lambda country : len(country) >= 6, countries))
print(num_6_or_more_countries)

#Ex7 Use filter to filter out countries starting with an 'E'
num_6_or_more_countries = list(filter(lambda country : country.startswith('E'), countries))
print(num_6_or_more_countries)

#Ex8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

#Ex9 Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

#Ex10 Use reduce to sum all the numbers in the numbers list.

#Ex11 Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

#Ex12 Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

#Ex13 Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

#Ex14 Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

#Ex15 Declare a get_last_ten_countries function that returns the last ten countries in the countries list.