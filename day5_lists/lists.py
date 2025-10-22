countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print('Countries:', countries)
print('Number of countries:', len(countries))

'''
--------------------------------
Data with baara
--------------------------------
'''
#* 1 - How to create a list
empty = []
print(empty)
print(type(empty))
empty = list()

letters = ['a', 'b', 'c', 'd']
print(empty)
print(type(empty))
print(letters)
print(type(letters))

letters2 = list('Python')
print(letters2)

matrix1 = [['a', 'b', 'c'], ['d', 'e', 'f']]
print(matrix1)

#* 2 - How to acces & read list
lst = ['a', 'b', 'c', 'd']
print(lst)
print(lst[0])
print(lst[-1])

matrix2 = [['a', 'b', 'c'], ['d', 'e', 'f'],['h', 'i' ,'j']]
print(matrix2)
print(matrix2[-1])
print(matrix2[-1][-1])
print(matrix2[0][0])

lst = ['a', 'b', 'c', 'd']
print(lst)
print(lst[:0])
print(lst[:-1])
print(lst[:])
print(lst[1:3])
matrix3 = [['a', 'b', 'c'], ['d', 'e', 'f'],['g', 'h' ,'i']]
print(matrix3[1:])
print(matrix3[-1][:2])
print(matrix3[2:][:3])

#* 3 - How to unpack list
person = ['Maria', 29, 'Data engineer', 'Spain']
# 1. Without unpacking
# name = person[0]
# age = person[1]
# role = person[2]
# country = person[3]

# 2. Unpacking
name, age, role, country = person 
print(role)

# Asteriks
name2, *details, country2 = person
print(name)
print(details)
print(country)

# Underscore
name, _, role, _ = person
print(name)
print(role)

# Asteriks & underscore
name, *_, country = person

#* 4 - Explore & Analyze Lists
numbers = [1,5,3,4,2,5]

#analyze
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Length of list:", len(numbers))

#completeness & existance check
print("All:", all(numbers))
print("All:", all([1 ,0 ,3]))
print("All:", all(['b', 'a', 'c']))
print("All:", all(['b', 'a', '']))
print("All:", any([]))
print("All:", any(['b', 'a', 'c']))
print("All:", any(['b', 'a', '']))
print("All:", any([0,0,0]))

#Search & count
print("Count", numbers.count(5))
print("Index of 3:", numbers.index(3))

#Membership & identity
print(4 in numbers)
print(8 in numbers)
print(8 not in numbers)
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)

#Comparison
print(list1 == list2)
list1 = [5,8,3]
list2 = [5,2,3]
print(list1 > list2) # python looks only on 1st index of both list if it is the same it go +1 index until one is bigger

#* 5 - How to add, remove and update list
letters = ['a', 'b', 'c']
letters.append('x')
letters.insert(1, 'y')
letters.insert(3, 'z')
print(letters)

matrix4 = [['a', 'b', 'c'], ['d', 'e', 'f'],['g', 'h' ,'i']]
matrix4.append(['x','y','z'])
matrix4.insert(0, ['a','a','a'])
matrix4[1].append('x')
matrix4[0].insert(0, 'z')
print(matrix4)



letters_t = ['a', 'b', 'c']
letters.clear()
print(letters_t)

letters = ['a', 'b', 'a']
letters.remove('a')
print(letters)

letters = ['a', 'b', 'c']
removed = letters.pop()
print(letters)
print('Removed Item:', removed)

matrix = [['a', 'b', 'c'], ['d', 'e', 'f'],['g', 'h' ,'i']]
# matrix.remove(['a', 'b', 'c'])
# matrix.pop()
matrix[1].remove('e')
matrix[-1].pop()
matrix[0].pop()
print(matrix)


letters = ['a', 'b', 'c']
letters[0] = 'x'
letters[1] = 'y'
letters = 'z'
print(letters)

#* 6 - How order list
letters = ['c', 'a', 'b']
letters.sort(reverse=True)
print(letters)

matrix = [
    ['d', 'e', 'f'],
    ['g', 'z' ,'i'],
    ['a', 'a', 'c']
]
matrix[1].sort()
print(matrix)

letters = ['c', 'a', 'b']
new_list = sorted(letters)
print(f"Sorted List: {new_list}")
print(f"Original List: {letters}")

letters = ['c', 'a', 'b']
#letters.reverse()
new_list = list(reversed(letters))
print('Original list', letters)
print('Reversed list', new_list)

#* 7 - How copy lists
#Assignment
letters = ['a', 'b', 'c']
letters_copy = letters.copy()
# letters_copy = letters
letters.pop()
letters_copy.append('z')
print('Original:',letters)
print('Copy:',letters_copy)

#Shallow copy
matrix = [
    ['a', 'b'],
    ['c', 'd']]
matrix_copy = matrix.copy()
matrix.pop()
matrix[0].append('z')
print('Original:',matrix)
print('Copy:',matrix_copy)

#Deep Copy
import copy
matrix = [
    ['a', 'b'],
    ['c', 'd']]
matrix_copy = copy.deepcopy(matrix)
matrix.pop()
matrix[0].append('z')
print('Original:',matrix)
print('Copy:',matrix_copy)


# IS operator
original = [
    ['a', 'b'],
    ['c', 'd']]
copy1 = original
print("Same Object?", original is copy1, "\n")


copy2 = original.copy()
print("Same Object?", original is copy2, "\n")
print("Shared Lists?", original[0] is copy2[0], "\n")

copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3, "\n")
print("Shared Lists?", original[0] is copy3[0], "\n")
#-------------------------------
'''
--------------------------------
Exercises
--------------------------------
'''
'''
#Ex Level 1 1-3
print('-' * 30)
newlist = []
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
print(f'length of the newlist = {len(newlist)}')
print(f'length of the countries = {len(countries)}')

#Ex 4
numbers = ['0', '1', '2', '3', '4', '5']
print(f'First item of list = {numbers[0]}')                     # Fist Item of list
print(f'Middle item of list = {numbers[int(len(numbers)/2)]}')  # Middle Item of list
print(f'Middle item of list = {numbers[-1]}')                   # Last Item of list

#Ex 5
mixed_data_types = ['Maciek', 20, 182, 'Married', 'Kielce']

#Ex 6 - 25
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)
print(f'There are {len(it_companies)} companies')
print(f'First company in list = {it_companies[0]}')                     # Fist Item of list
print(f'Middle company in list = {it_companies[int(len(numbers)/2)]}')  # Middle Item of list
print(f'Middle company in list = {it_companies[-1]}')                   # Last Item of list

it_companies[0] = 'HP'
print(it_companies)

it_companies.append('VirtusLab')

it_companies.insert((len(it_companies) // 2), 'Comarch')

it_companies[1] = it_companies[1].upper()

joined_companies = '#;  '.join(it_companies)
print(joined_companies)

does_exist = 'Apple' in it_companies 
print(does_exist)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[0:3])

print(it_companies[-3:])

print(it_companies[(len(it_companies) // 2):round(len(it_companies) / 2) + 1])

it_companies.remove('VirtusLab')

it_companies.pop(len(it_companies) // 2)

it_companies.pop(-1)

it_companies.clear()

del it_companies

#Ex 26,27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined = front_end + back_end
print(joined)

full_stack = joined.copy()
full_stack.insert(5, 'Python')
full_stack.insert(5, 'SQL')
print(full_stack)

#--------------------------------
#Exercises Level 2
#--------------------------------

# Ex 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages.append(min(ages)))
print(ages.append(max(ages)))
ages = sorted(ages)
print(ages)
if len(ages) % 2 == 0:
    print( sum ( ages [len(ages) // 2 - 1:len(ages) // 2 + 1] ) / 2)
else:
    print(ages[len(ages) // 2])

sum_age = sum(ages)
print(sum_age / len(ages))

range = max(ages) - min(ages)
print(range)

print(abs(min(ages) - sum_age / len(ages)))
print(abs(max(ages) - sum_age / len(ages)))


import sys, os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from countries import countries

if len(countries) % 2 == 0:
    print(countries[len(countries) // 2 - 1:len(countries) // 2 + 1] )
else:
    print(countries[len(countries) // 2])

def split_countries(countries):
    mid = (len(countries) + 1) // 2  # Ensures the first half gets one more if odd
    first_half = countries[:mid]
    second_half = countries[mid:]
    return first_half, second_half

# Example usage:
first, second = split_countries(countries)

print("First half:", first)
print('-' * 50)
print("Second half:", second)

c2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
China, Russia, USA, *Scandic = c2
print(Scandic)
'''