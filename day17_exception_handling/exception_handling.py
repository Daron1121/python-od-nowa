# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2025 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except:
#     print('Something went wrong')


# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occur')
# except ValueError:
#     print('Value error occur')
# except ZeroDivisionError:
#     print('zero division error occur')
# else:
#     print('I usually run with the try block')
# finally:
#     print('I alway run.')


# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2025 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except Exception as e:
#     print(e)


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15


def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))


lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']


for index, item in enumerate([20, 30, 40]):
    print(index, item)

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

#* Exercises
#Ex 1 Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print(nordic_countries)
print(es)
print(ru)

#  PART 1: Exception Handling
#  Exercise 1: Division Error
# Write a program that:
# Asks the user for two numbers,
# Tries to divide them, Gracefully handles:ZeroDivisionError, ValueError, any other unexpected exception
int1 = input("Input number 1 : ")
int2 = input("Input number 2 : ")
try:
    division = int(int1) / int(int2)
    print(f"The result is: {division}")
except ZeroDivisionError as e:
    print(f'Int2 cant be 0 - {e}')
except ValueError as v:
    print(f'You need to provide integer! - {v}')
except Exception as ae:
    print(f"Something went wrong - {ae}")
finally:
    print("Program finished.")

# Exercise 2: File Handling
# Write a program that tries to open a file called "data.txt".
# If the file doesn’t exist, print "File not found" instead of crashing.
try:
    open("data.txt")
except FileNotFoundError as e:
    print(f"File not found - {e}")

# Exercise 3: Exception with Feedback
# Ask the user for their name and year of birth.
# Try to calculate their age.
# If the input is invalid, print the exact error using:
# except Exception as e:
#   print(e)
name = input("Enter your name: ")
year_of_birth = input("Enter your year of birth: ")
try:
    age = 2025 - int(year_of_birth)
except Exception as e:
    print(e)


    

# todo PART 2: Packing & Unpacking
# Exercise 4: Unpacking Lists
# You have a list:
# numbers = [5, 10, 15, 20, 25, 30, 35]
# Unpack it so that:
# The first two numbers go into a and b,
# The remaining numbers go into rest.
# Then print:
# a = 5, b = 10, rest = [15, 20, 25, 30, 35]

# Exercise 5: Unpacking Dictionaries
# Write a function:
# def describe_person(name, country, city, age):
#     ...
# and a dictionary:
# person = {"name": "Alice", "country": "Norway", "city": "Oslo", "age": 28}
# Use unpacking (**person) to call the function.


# Exercise 6: Packing with *args
# Create a function multiply_all(*args) that multiplies any number of numbers together.
# Example:
# print(multiply_all(2, 3, 4))  # 24
# print(multiply_all(1, 5, 10, 2))  # 100

# 🎁 Exercise 7: Packing with **kwargs
# Create a function print_student_info(**kwargs) that prints any information passed about a student:
# print_student_info(name="John", age=20, course="Python")
# Expected output:
# name = John
# age = 20
# course = Python

# 🌀 PART 3: Spreading
# 🌍 Exercise 8: Spread Lists

# You have:
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# Combine them using the spread (*) operator into a new list:
# [0, *list1, *list2, 7, 8]
# Expected:
# [0, 1, 2, 3, 4, 5, 6, 7, 8]


# 🔢 PART 4: Enumerate & Zip
# 🧾 Exercise 9: Enumerate
# You have:
# countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
# Use enumerate() to print:
# 0 Finland
# 1 Sweden
# 2 Norway
# ...

# 🧾 Exercise 10: Find a Country
# Using the same list, print:
# Finland found at index 0
# if "Finland" is in the list (use enumerate and if).

# 🔗 Exercise 11: Zip
# You have two lists:
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 90, 78]
# Use zip() to loop through them and print:
# Alice got 85 points
# Bob got 90 points
# Charlie got 78 points

# 💡 Bonus Challenge:
# Combine zip + enumerate to print:
# 1. Alice - 85
# 2. Bob - 90
# 3. Charlie - 78