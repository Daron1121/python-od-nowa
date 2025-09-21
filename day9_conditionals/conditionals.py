score = 25
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