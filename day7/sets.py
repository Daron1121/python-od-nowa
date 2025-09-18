# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)

print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True

st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits.pop())  # removes a random item from the set

# Joining Sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}


# Intersection
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}

#subset & superset
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True


#differance betwen sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}

#Finding Symmetric Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
#----------------------------------------------------------------------------------------------------
print(40 * '-')
print("Exercises")
print(40 * '-')
print("LVL 1")



it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Ex 1
print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

new_companies = ["Commarch", 'Virtus Lab', 'Webplace']
it_companies.update(new_companies)
print(it_companies)

it_companies.remove('Webplace')
print(it_companies)

#What is the difference between remove and discard
#Remove make errors if value that is removed doesnt exist in the set, discard avoid errors
it_companies.discard("a")
print(it_companies)
#it_companies.remove("")

print(40 * '-')
print("LVL 2")

print(A.union(B))

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))

del A
del B

print(40 * '-')
print("LVL 3")


print(len(age))
print(len(set(age)))
# Jest roznica w wielkosci poniewaz przy zmianie na set usuwane sa powtorki z listy


#Explain the difference between the following data types: string, list, tuple and set
'''
string - data type that contains plain text
list - data type/structure that can have duplicates, and is indexed and modifiable and ordered
tuple - data type/structure that can have duplicates, and CANT change values for entire program, is unmodifable and ordered
set - data type/structure that CANT have duplicates, is not indexed,unmodifable, and is randomized
'''

#How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
a = "I am a teacher and I love to inspire and teach people".split()
print(set(a))
print(f"There are {len(set(a))} unique words")