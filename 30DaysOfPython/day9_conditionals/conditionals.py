score = 81
project = True 
if score >= 95 and project:
    print("A+")
elif score >= 95:
    print("A")
elif score >= 80:
    print("B")
elif score >= 75:
    print("C")
elif score >= 50:
    print("D")
elif score >= 30 or project:
    print("E")
else:
    print("F")

#Inline if (Ternary)
ocena = "A" if score >= 90 else 'F'
print(ocena)

ocena2 = "A" if score >= 90 else "B" if score >= 80 else "F"
print(ocena2)

country = "United States"
'''
Normally:
if country == "United States"
elif
elif ... etc.



Better to use match case!!
'''
#Match-case
match country:
    case "United States":
        print("US")
    case "India":
        print("IN")
    case "Egipt":
        print("EG")
    case "Germany":
        print("GE")
    case _:
        print("Unknown country")
    



#Exercise 1 - Data With Baara
'''
Validate the Quality and Correctness of Email Values
'''

email = 'filipterelak1@gmail.com'

#Clean the string
email = email.strip()

#Email must not be empty
if email == "":
    print("Your email is empty!!")
#Email must contain a '.' or '@'
elif '.' not in email or '@' not in email or email.find('@') != email.rfind('@'):
    print("Your email dont have either '.' or '@'")
#Email must contain exacly one '@' symbol
elif email.find('@') != email.rfind('@'):
    print('Your email must contain exacly one @')
#Email must end with '.com', '.org' or '.net'
elif str(email[-4:]) not in ['.com', '.org', '.net']:
    print("Your email must have valid domain")
#Email must not be longer than 254 characters
elif len(email) > 254:
    print('Your email is too long')
#Email must start and end with a letter or digit
elif not (email[0].isalnum() and email[-1].isalnum()):
    print('Email must start with a letter or digit')
else:
    print("Your email is valid")

#Exercise 2 - Data With Baara
'''
Validate the Quality and Correctness of Password Values
'''
password = 'abcDefgh1j'
password = password.strip()

if password == "":
    print("Your password is empty!!")
elif len(password) < 8:
    print("Your password must contain at least 8 characters")
elif password == email:
    print("Your password cant be same as email")
elif not any(char.isupper() for char in password):
    print('Your password must contain a uppercase')
elif not any(char.islower() for char in password):
    print('Your password must contain a lowercase')
elif password.find(' ') != -1:
    print("Your password cant have spaces")
elif not (password[0].isalnum() and password[-1].isalnum()):
    print('Password must start with a letter or digit')
else:
    print('Your password is valid')

print("-" * 50)
#Exercises from 30DaysOfPython
#LEVEL 1
#Ex 1
age = input("Enter your age: ")
if int(age) >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18-int(age)} more years to learn to drive.')

#Ex 2
my_age = 17
your_age = int(input("Enter your age: "))
if my_age > your_age:
    print(f'You are {my_age-your_age} year(s) youger than me!')
else:
    print(f'You are {your_age-my_age} year(s) older than me!')

#Ex 3
a = input("Give number a: ")
b = input("Give number b: ")

if a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"a: {a} is same than b: {b}")
else:
    print(f"a: {a} is smaller than b: {b}")


#LEVEL 2
#Ex 1
score = 25
if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")

month = input("Enter Month (January, February, March, April, May, June, July, August, September, October, November, December)")

if month in ['March', 'April', 'May']:
    print('Its Spring!')
elif month in ['June', 'July', 'August']:
    print('Its Summer!')
elif month in ['September', 'October', 'November']:
    print('Its Autumn!')
else:
    print('Its Winter!')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("type fruit")
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print('That fruit already exist in the list')

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person.keys():
    print(person['skills'][len(person['skills'])// 2])

#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person.keys():
    print('Python' in person['skills'])

# * -------------------------------------------------------------------------------------
# * HARDEST CHALLANGE!!!!!!!!!!!!!!!
# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'React' in person['skills']:
    if 'Node' and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')
    elif 'JavaScript' in person['skills']:
        print('He is a front end developer')
elif 'Node' and 'MongoDB' in person['skills']:
    if 'React' in person['skills']:
        print('He is a fullstack developer')
    elif 'Python' in person['skills']:
        print('He is a backend developer')
else:
    print('unknown title')

# * -------------------------------------------------------------------------------------

#If the person is married and if he lives in Finland, print the information in the following format:
if person['is_marred'] and person['country'] == 'Finland':
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married')