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

#Ex 1
print('Coding ' + 'for ' + 'all')