person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

print('-' * 30)
for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

#* Break
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
#* Continue
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

#------------------------------------------------------------------------------------
#* Exercises: Day 10 30DaysOfPython
#* Exercises: Level 1
#Ex 1
for iter in range(11):
    print(iter)
print(30* '-')
iterated = 0
while iterated < 11:
    print(iterated)
    iterated += 1


#Ex 2
for iter1 in range(11, 0):
    print(iter1)
print(30* '-')
iterated = 11
while iterated < 11:
    print(iterated)
    iterated -= 1

#Ex 3
for x in range(8):
    print('#' * x)

#todo Ex 4


#Ex 5
print(30* '-')
for liczba in range(11):
    print(f'{liczba} x {liczba} = {liczba*liczba}')


#Ex 6
lista = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in lista:
    print(item)

#Ex 7,8
for liczby in range(101):
    if liczby % 2 == 0:
        print(liczby)
for liczby in range(101):
    if liczby % 2 != 0:
        print(liczby)


#* Exercises: Level 2