person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['age'])
person['age'] = 252
print(person['age'])
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item
#----------------------------------------------------------------------------------------------------
print(40 * '-')
print("Exercises")
print(40 * '-')
print("LVL 1")

#Ex 1,2
dog = {
    'name':'Pluto',
    'color':'Yellow',
    'breed':'Dobberman',
    'legs':4,
    'age':3
}

#Ex 3-11
student = {
    'first_name':'Filip',
    'last_name':'Terelak',
    'gender':'Male',
    'age':17,
    'marital status':'S',
    'skills':['SQL','Git','Python'],
    'country':'Poland',
    'city':'Warsaw',
    'address':'Y',
}
print(len(student))
print(student['skills'])
print(type(student['skills']))

student['skills'].append('Spark')
student['skills'].append('GitHub')
print(student['skills'])

print(student.keys())
print(student.values())

print(student.items())

print(student.pop('address'))
print(student)

del student

#* DataWithBaraa - Episode

my_dict = {'a': 10, 'b': 20, 'c': 30}
print(my_dict)

print(my_dict['c'])
# Dict - Ordered, Keys are unique, values allow duplicated, not indexed(Keyed), mutable

user = {'id':1, 'age':30, 'city':'Berlin'}
#Access
print(user['id'])

# print(user['name']) #* access by '[]' throws keyerror if key doesnt exist
print(user.get('name', 'Unknown'))

#Checks
print('age' in user)
print('name' not in user)

#View Objects
print(user.keys())
print(user.values())
print(user.items())

#Looping
for u in user:
    print(u, user[u])

for key, value in user.items(): # Better option!
    print(key, value)

#Add, Remove, Update
user['name'] = 'John' #Adding new value

user['age'] = '35' #Update value

user.update({'age':40, 'city':'Paris'})
print(user)

age = user.pop('age')
salary = user.pop('salary', "Not Found") # It key doesnt exist we get error, we can go around that by defining message after that
print(user)
print(f'Removed item: {age}')
print(f'Removed item: {salary}')

#Creation
user = {'id': None, 'name':None, 'age':None, 'city':None} 
user = dict.fromkeys(['id','name','age','city'], None) #this fucntion does same as the example above
print(user)

#Challange
user = {'id': 1, 'name':'John', 'age':30, 'city':'Berlin'}

# output = {}
# for key,value in user.items():
#     if isinstance(value, str):
#         output[key] = value.upper()
#     else:
#         continue
# print(output)

#! OR

output = { key:value.upper() for key,value in user.items() if isinstance(value, str)}
print(output) 

#1 Create an empty dictionary called dog 
#2 Add name, color, breed, legs, age to the dog dictionary
dog = {}
dog = dog.fromkeys(['name','color','breed','legs','age'], None)
print(dog)
#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'Filip', 'last_name':'Terelak', 'gender':'Male', 'age':'18', 'marital status':'Single', 'skills':['Python', 'SQL', 'Git', 'MsFabric', 'PySpark'], 'country':'PL', 'city':'Random', 'address':'123B Ulica'}
print(student)
#4 Get the length of the student dictionary
print(len(student))
#5 Get the value of skills and check the data type, it should be a list
print(student['skills'])
#6 Modify the skills values by adding one or two skills
student['skills'].extend(['Math','Azure'])
print(student)
#7 Get the dictionary keys as a list
print(student.keys())
#8 Get the dictionary values as a list
print(student.values())
#9 Change the dictionary to a list of tuples using items() method
print(student.items())
#10 Delete one of the items in the dictionary
student.pop('address')
#11 Delete one of the dictionaries
del student
print(student)