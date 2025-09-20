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