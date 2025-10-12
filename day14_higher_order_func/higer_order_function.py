
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
reduce - it returns a single value that represent the output of function in iterable
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
result = reduce(
    lambda acc, country: acc + [country] if 'LAND' in country else acc,
    filter(lambda c: len(c) >= 6, map(lambda c: c.upper(), countries)),
    []
)
print(result)
#Ex9 Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lista):
    nowa_l = list(map(lambda x: str(x), lista))
    return nowa_l
print(get_string_lists([3, 'dsc', True]))

#Ex10 Use reduce to sum all the numbers in the numbers list.
suma = reduce(lambda s , s2 : s + s2, numbers)
print(suma)

#Ex11 Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
concating = reduce(lambda acc, country: f"{acc}, {country}" if country != countries[-1] else f"{acc}, and {country}",countries[1:],countries[0]) +'are north European countries'
print(concating)

#Ex12 Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from countries import countries

def categorize_countries(lista):
    nowe = []
    for country in lista:
        if 'land' in country or 'ia' in country or 'island' in country or 'stan' in country :
            nowe.append(country)
    return nowe
print(categorize_countries(countries))

#Ex13 Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def names_of_country(countries):
    dictio = {}
    for country in countries:
        first_letter = country[0].upper()
        dictio[first_letter] = dictio.get(first_letter, 0) + 1
    return dictio

print(names_of_country(countries))

#Ex14 Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(lista):
    return lista[:10]
print(get_first_ten_countries(countries))

#Ex15 Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(lista):
    return lista[-10:]
print(get_last_ten_countries(countries))

#* Exercises: Level 3
#Ex 1Use the countries_data.py file and follow the tasks below:
from countries_data import nowalista
# Sort countries by name, by capital, by population
from countries_data import nowalista

# Sort countries by name, by capital, by population
def sorting_function(countries: list):
    # Sort by name
    sorted_by_name = sorted(countries, key=lambda c: c["name"])

    # Sort by capital
    sorted_by_capital = sorted(countries, key=lambda c: c["capital"])

    # Sort by population
    sorted_by_population = sorted(countries, key=lambda c: c["population"], reverse=True)

    return sorted_by_name, sorted_by_capital, sorted_by_population


# Example usage:
sorted_name, sorted_capital, sorted_population = sorting_function(nowalista)

print("Sorted by name:")
for c in sorted_name[:5]:
    print(c["name"])

print("\nSorted by capital:")
for c in sorted_capital[:5]:
    print(c["capital"])

print("\nSorted by population (top 5):")
for c in sorted_population[:5]:
    print(f"{c['name']} — {c['population']}")

# Sort out the ten most spoken languages by location.
# Sort out the ten most populated countries.