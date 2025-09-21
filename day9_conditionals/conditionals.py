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

#Exercise - Data With Baara
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



'''
if len(email) > 254:
    print('Too long')
'''