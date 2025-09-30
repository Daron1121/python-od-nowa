# syntax
# Declaring a function
def function_name():
    pass
# Calling a function
function_name()
#--------------------------------------------------------
# Function can be declared without parameters.
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
print(f'Function return : {generate_full_name()}')  

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
print(f'Function return : {add_two_numbers()}')
#--------------------------------------------------------
print(50* '-')
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(f'Function return : {generate_full_name()}')                  #* output is the returned value

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(f'Function return : {add_two_numbers()}')                     #* output is the returned value
#--------------------------------------------------------
print(50* '-')
# syntax
# Declaring a function
def function_name(parameter):
    pass
# Calling function
argument = ''
print(function_name(argument))



def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

#--------------------------------------------------------
print(50* '-')

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

#--------------------------------------------------------
print(50* '-')
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10

#--------------------------------------------------------
#* Exercises
#--------------------------------------------------------
print(50* '-')

#* Exercises: Level 1
#Ex 1
def add_two_numbers(a, b):
    sum = a + b
    return sum
print(add_two_numbers(5, 4))

#Ex 2
def area_of_circle(r):
    pi = 3.14
    return pi * r * r
print(area_of_circle(4))

#Ex 3
def add_all_nums(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
print(add_all_nums(9,8,7,6,5))

#Ex 4
def convert_celsius_to_fahrenheit(cel):
    F = (cel * 9/5) + 32
    return F
print(convert_celsius_to_fahrenheit(0))

#Ex 5
def pora_roku(miesiac):
    if miesiac in ['March', 'April', 'May']:
        print('Its Spring!')
    elif miesiac in ['June', 'July', 'August']:
        print('Its Summer!')
    elif miesiac in ['September', 'October', 'November']:
        print('Its Autumn!')
    else:
        print('Its Winter!')
miesiac_1 = 'March'
pora_roku(miesiac_1)

#Ex 6
def calculate_slope(x1, y1,x2,y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(9,6,5,7))

import cmath
#Ex 7
def solve_quadratic_eqn(a,b,c):
    D = b**2 - 4*a*c
    x1 = (-b - cmath.sqrt(D)) / (2 * a)
    x2 = (-b + cmath.sqrt(D)) / (2 * a)
    return x1,x2
print(solve_quadratic_eqn(2,5,2))

#Ex 8
def print_list(lista):
    for iter in lista:
        print(iter)
print_list(['a','b','c','d'])

#todo Ex 9
def reverse_list(array):
    pass

#Ex 10
def capitalize_list_items(lista):
    for item in lista:
        print(item.upper())
capitalize_list_items(['a','b','c','d'])

# Ex 11
def add_item(list, do_dodania):
    return list.append(do_dodania)
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))    
print(food_staff)

#Ex 12
def remove_item(jaka_lista, co):
    return jaka_lista.remove(co)
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
print(food_staff)

#Ex 13
def sum_of_numbers(number):
    return sum(range(number + 1))
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))