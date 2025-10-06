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
filters = [i for i in numbers if i <= 0]
print(filters)

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

#------------------------------------------------
#ChatGPT exercises for lambda:
#* LVL 1
# Utwórz lambdę, która przyjmuje jedną liczbę i zwraca jej kwadrat.
# Następnie wywołaj ją dla liczby 5.
kwadrat = lambda arg1 : arg1**2
print(kwadrat(5))

# Suma dwóch liczb
# Napisz lambdę, która dodaje dwie liczby i zwraca wynik.
# Wywołaj ją dla 3 i 7.
suma = lambda arg1, arg2 : arg1 + arg2 
print(suma(3,7))

# Sprawdzenie parzystości
# Napisz lambdę, która sprawdza, czy liczba jest parzysta (zwraca True lub False).
# Przetestuj dla kilku liczb.
parzystosc = lambda liczba :liczba % 2 == 0
print(parzystosc(4))
print(parzystosc(62))
print(parzystosc(7))
print(parzystosc(109))

#* LVL 2

# Sortowanie z lambdą
# Mając listę słów:
words = ["python", "lambda", "map", "filter", "reduce"]
# Posortuj je wg długości słowa przy użyciu funkcji sorted() i lambdy.
sortowanie = lambda lista : sorted(lista, key = lambda x : len(x)) # key - klucz czyli po czym funkcja sorted ma sortowac
print(sortowanie(words))

# Filtrowanie z lambdą
# Mając listę liczb 
numbers = [1, 4, 7, 10, 13, 16]
# użyj filter() i lambdy, aby zostawić tylko liczby większe niż 8.
wieksze = lambda lista: list(filter(lambda x: x > 8, lista))
print(wieksze(numbers))

# Mapowanie z lambdą
# Mając listę 
nums = [1, 2, 3, 4, 5]
# użyj map() i lambdy, aby otrzymać listę kwadratów tych liczb.
mapowanie = lambda lista: list(map(lambda x: x**2, lista))
print(mapowanie(nums))
#* LVL 3

# Redukcja z lambdą
# Mając listę 
nums = [1, 2, 3, 4, 5]
# użyj reduce() i lambdy, aby obliczyć iloczyn wszystkich elementów.
# (Importuj reduce z functools.)
from functools import reduce
redukcja = lambda lista: reduce(lambda x,y : x*y, lista)
print(redukcja(nums))

# Zagnieżdżona lambda
# Utwórz lambdę, która przyjmuje liczbę i zwraca inną lambdę, która dodaje do niej podany argument.
# Przykład:

# add_five = make_adder(5)
# print(add_five(3))  # powinno dać 8
make_adder = lambda x: (lambda y: x + y)

add_five = make_adder(5)   
print(add_five(3))        
print(add_five(10))       

add_ten = make_adder(10)   
print(add_ten(7))           

#!add_number = lambda x : x + int(input(f"Co Chcesz dodad do {x} "))
#!print(add_number(5))

# Sortowanie po wielu kryteriach
# Mając listę krotek:
data = [("Ala", 25), ("Bartek", 20), ("Celina", 25), ("Dawid", 19)]
# Posortuj najpierw po wieku rosnąco, a w przypadku remisu — alfabetycznie po imieniu.
posortowane = lambda lista : sorted(lista, key=lambda x: (x[1], x[0]))
print(posortowane(data))

# Lambda w funkcji key z max()
# Mając listę słów 
zwierzeta = ["kot", "pies", "hipopotam", "lew"]
# znajdź najdłuższe słowo przy pomocy max() i lambdy.
najdluzsze = lambda lista : max(lista, key=lambda x : len(x))
print(najdluzsze(zwierzeta))