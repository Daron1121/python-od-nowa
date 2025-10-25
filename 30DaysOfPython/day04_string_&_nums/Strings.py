print('------------------------------------------------------------------------')
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'

#Old style formatting
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

#New style formatting
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

#string interpolation / f-strings
print(f'I am {first_name} {last_name}. I teach {language}')

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print('------------------------------------------------------------------------')
'''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
| Recap of string formatting in Python |
========================================

========================================
Exercise of Day 4
----------------------------------------
'''
#Ex 1
print('Thirty ' + 'Days ' + 'Of ' + 'Python')

#Ex 2
print('Coding ' + 'for ' + 'all')

#Ex 3 - 11
company = "Coding For All"

print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[:6])
#Lub
first_space_index = company.find(" ")
print(company[first_space_index + 1:])


print(company.index('Coding'))
print(company.find('Coding'))


print(company.replace(company, 'Python'))
#Ex 12
text = 'Python For Everyone'

print(text.replace('Everyone', 'All'))
#Ex 13
print(company.split(' '))

#Ex 14
a = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(a.split(','))

#Ex 15
print(company[0])

#Ex 16
print(company[len(company) - 1])

#Ex 17
print(company[10])

#Ex 18
text = "Python For Everyone"
acronym = ''.join(word[0].upper() for word in text.split())
print("Acronym:", acronym)

#Ex 19
acronym2 = ''.join(word[0].upper() for word in company.split())
print("Acronym:", acronym2)

#Ex 20 - 22
print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

#Ex 23 - 24
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))

print('You cannot end a sentence with because because because is a conjunction'.index('because'))
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))

#Ex 25
print("You cannot end a sentence with because because because is a conjunction".replace("because because because", ""))

#Ex 26
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

#Ex 27
print("You cannot end a sentence with because because because is a conjunction".replace("because because because", ""))

#Ex 28, 29
print(company.startswith('Coding'))

print(company.startswith('coding'))

#Ex 30
print('   Coding For All      ' .strip())

#Ex 31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

#Ex 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(libraries)
print(result)

#Ex 33
print('I am enjoying this challenge.\nI just wonder what is next.')

#Ex 34
print('Name\t Age\tCountry\tCity\nAsabeneh 250 \tFinland Helsinki')

#Ex 35
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {int(area)} meters square.')

#Ex 36
print(f"""
8 + 6 = {8 + 6}
8 - 6 = {8 - 6}
8 * 6 = {8 * 6}
8 / 6 = {8 / 6}
8 % 6 = {8 % 6}
8 // 6 = {8 // 6}
8 ** 6 = {8 ** 6}""")

'''
========================================
DwB - practise
----------------------------------------
'''

day = "2026/05/10"
transf_day = day.replace('/', '-')
print(transf_day)

phone_num = "+49 (176) 123-4567"
transf_num = phone_num.replace('+49', '0049').replace('(','').replace(')','').replace('-','').replace(' ','')
print(transf_num)

casv_file = "123,max,USA,1970-10-05,M"
print(casv_file.split(","))

'''
----------------------------------------
Indexing & Slicing
----------------------------------------
'''
text = "Python"
print(text[0])
print(text[-1])
print(text[3])

date = "2025-09-12"

# Extract the year
print(date[0:4])

# Extract the month
print(date[5:7])

# Extract the day
print(date[-2:])

to_clean = "968-Maria, ( D@t@ Engineer );; 27y  "
converted = to_clean.replace("968-", 'name: ').replace('D@t@', 'data').replace('(', '| role:').replace(')', '').replace(',', '').replace(';;', '| age:').replace('y', '').strip().lower()
print(converted)