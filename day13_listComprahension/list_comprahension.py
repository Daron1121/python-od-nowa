language = 'Python'

# One way
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']
#--------------------------------------------------------------------------
print(50* '-')
# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#* Exercises
#Ex 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter = [i for i in numbers if i <= 0]
print(filter)

#Ex 2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [i for sublist in list_of_lists for inner in sublist for i in inner]
print(flattened)

#Ex 3
l_comp = [(i,1,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
for t in l_comp:
    print(t)

#Ex 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[first.upper(), first.upper()[:3], last] for sublist in countries for first, last in sublist]
print(output)
#Ex 5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [{'country': first.upper(), 'city': last.upper()} for sublist in countries for first, last in sublist]
print(output)

#Ex 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [f"{first} {last}" for sublist in names for first, last in sublist]
print(output)

#Ex 7
x1,y1 = 2,3
x2,y2 = 5,11
slope = lambda x1,y1,x2,y2 : (y2-y1)/(x2-x1)
print(slope(x1,y1,x2,y2))