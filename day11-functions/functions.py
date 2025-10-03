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

#Ex 9
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):  # loop from last index down to 0
        reversed_arr.append(arr[i])
    return reversed_arr
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

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

# Ex 14
def sum_of_odds(number):
    sum = 0
    for odd in range(number + 1):
        if odd % 2 == 0:
            sum += odd
    return sum
print(sum_of_odds(5))

# Ex 15
def sum_of_even(number):
    sum = 0
    for even in range(number + 1):
        if even % 2 != 0:
            sum += even
    return sum
print(sum_of_even(5))

#* LEVEL 2
# Ex 1
def evens_and_odds(numbers):
    even = 0
    odds = 0
    for number in range(numbers + 1):
        if number % 2 == 0:
            odds += 1
        else:
            even += 1
    print(f"The number of odds are {odds}") 
    print(f"The number of even are {even}") 
evens_and_odds(100)

# Ex 1
def factorial(factor):
    output1 = 1
    for number in range(1, factor + 1):
        output1 *= number
    return output1
print(factorial(8))

# Ex 2
def is_empty(parameter):
    pass

# Ex 3
def calculate_mean(lista):
    suma = 0
    for number in lista:
        suma += number
    lenght = 0
    for index in lista:
        lenght += 1
    return suma / lenght
print(calculate_mean([5,4,3,2,1]))

def calculate_median(lista):
    for _ in range(len(lista) - 1):            
        for i in range(len(lista) - 1):     
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    n = len(lista)
    mid = n // 2

    if n % 2 != 0:
        return lista[mid]
    else:
        return ((lista[mid - 1] + lista[mid]) / 2) 

print(calculate_median([5,4,3,2,1,6]))

def calculate_mode(lista):
    counts = {}
    for iter in lista:
        if iter not in counts:
            counts[iter] = 1
        else:
            counts[iter] += 1
    sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1]))
    a = sorted_dict.popitem()
    return f"Item {a[0]} is mode of this list , and it occured {a[1]} time(s)"
print(calculate_mode([5,2,6,1,1,1,3,4,3,2,6,1,6]))

def calculate_range(lista):
    for _ in range(len(lista) - 1):
        for iter in range(len(lista) - 1):
            if lista[iter] > lista[iter + 1]:
                lista[iter] , lista[iter + 1] = lista[iter + 1] , lista[iter]
    return f"The range is euqal {lista[-1] - lista[0]}"
print(calculate_range([5,2,6,1,1,1,3,4,3,2,6,1,6]))

def calculate_variance(lista):
    # 1 step - calculate mean
    mean = 0
    for i in lista:
        mean += i
    mean = round(mean/len(lista) , 2)
    
    # 2 step - calculate devitation
    devitation = {}
    for iter in lista:
        devitation[iter] = round((iter - mean),2)
    print(devitation) 

    devitation = devitation.values()
    devitation = list(devitation)
    # 3 step - Square the Deviations
    sq_deva = []
    for iter in devitation:
        iter = round(iter ** 2,2)
        sq_deva.append(iter)
    print(sq_deva)

    # 4 step - Sum the Squared Deviations
    sum_of_sqrs = 0
    for iter in sq_deva:
        sum_of_sqrs += iter


    # 5 step - Sample Variance !Last
    # Divide the sum of squares by the number of data points minus one (n - 1)
    s_variance = sum_of_sqrs/len(lista) - 1
    return f"The sample variance of this list is: {s_variance}"
print(calculate_variance([3,2,6,1,1,1,3,4,3,2,6,1,6]))

import cmath
def calculate_std(lista):
    # 1 step - calculate mean
    mean = 0
    for i in lista:
        mean += i
    mean = round(mean/len(lista) , 2)
    
    # 2 step - calculate devitation
    devitation = {}
    for iter in lista:
        devitation[iter] = round((iter - mean),2)
    print(devitation) 

    devitation = devitation.values()
    devitation = list(devitation)
    # 3 step - Square the Deviations
    sq_deva = []
    for iter in devitation:
        iter = round(iter ** 2,2)
        sq_deva.append(iter)
    print(sq_deva)

    # 4 step - Sum the Squared Deviations
    sum_of_sqrs = 0
    for iter in sq_deva:
        sum_of_sqrs += iter


    # 5 step - Sample Variance !Last
    # Divide the sum of squares by the number of data points minus one (n - 1)
    s_variance = sum_of_sqrs/len(lista) - 1

    # 6 setp - Find the Standard Deviation
    return cmath.sqrt(s_variance)
print(calculate_std([3,2,6,1,1,1,3,4,3,2,6,1,6]))

#* LEVEL 3
# Ex 1
def is_prime(number):
    dzielniki = []
    for i in range(1, number + 1):
        if number % i == 0:
            dzielniki.append(i)
    if len(dzielniki) != 2:
        return 'Not Prime Number'
    else:
        return "Prime Number"
print(is_prime(9))

#Ex 2 
def check_list(lista):
    for _ in range(len(lista) - 1):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    for i in range(len(lista) - 1):
        if lista[i] == lista[i+1]:
            return f'List {lista} has not only unique items'
        else:
            return f'List {lista} has only unique items'
    print(lista)
print(check_list([1,2,3,6,9,8]))

#Ex 3

#Ex 4

#Ex 5