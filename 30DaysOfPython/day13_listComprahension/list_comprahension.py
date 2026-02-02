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


#Dodatkowe cwiczenia chat gpt
#proste labdy
# Ostatnia cyfra liczby
# Utwórz lambdę, która zwraca ostatnią cyfrę liczby.

ostatnia_cyfra = lambda n: n % 10
print(ostatnia_cyfra(12345))  # -> 5


# Wartość bezwzględna
# Lambda, która zwraca wartość bezwzględną liczby (bez użycia abs()).

wartosc_bezwzgledna = lambda n: n if n >= 0 else -n
print(wartosc_bezwzgledna(-10))  # -> 10


# Zamiana na wielkie litery
# Lambda, która przyjmuje string i zwraca go dużymi literami.

duze = lambda s: s.upper()
print(duze("python"))  # -> PYTHON


# Pierwsza litera
# Lambda, która zwraca pierwszą literę danego słowa.

pierwsza = lambda s: s[0] if s else None
print(pierwsza("Lambda"))  # -> L

# 🟡 LVL 2 — Lambdy z map/filter/sorted

# Filtrowanie liczb parzystych i nieparzystych
liczby = list(range(1, 21))
parzyste = list(filter(lambda n : n%2 == 0, liczby))
nieparzyste = list(filter(lambda n : n%2 != 0, liczby))
print(parzyste)
print(nieparzyste)

# Podwajanie elementów
# Użyj map(), by każdy element listy pomnożyć przez 2.
liczby = [2, 5, 8, 11]
nowe_liczby = lambda liczby : list(map(lambda x : x*2, liczby))
print(nowe_liczby(liczby))

# Słowa dłuższe niż 4 litery
slowa = ["kot", "hipopotam", "lew", "zebra", "papuga"]
dluzsze = lambda slowo : list(filter(lambda x: len(x) > 4, slowa))
print(dluzsze(slowa))

# Sortowanie po ostatniej literze
slowa = ["kot", "pies", "lew", "papuga"]
sortowanie = lambda slowo : list(sorted(slowo, key= lambda x: x[-1]))
print(sortowanie(slowa))
# 🔵 LVL 3 — Kombinacje i funkcje wyższego rzędu

# Reduce — suma cyfr liczby

from functools import reduce
liczba = 12345
cyfry = list(map(int, str(liczba)))

suma_c = lambda liczby: reduce(lambda n,m : n + m, str(liczby))
print(suma_c(cyfry))


# Tworzenie funkcji z lambdy (closure)
# Utwórz lambdę make_multiplier, która zwraca inną lambdę mnożącą przez określoną liczbę:
make_multiplier = lambda n : (lambda x: x * n)
times3 = make_multiplier(3)
print(times3(10))  # -> 30


# Zagnieżdżona lista comprehension z warunkiem
# Wygeneruj listę kwadratów liczb parzystych z zakresu 0–20:
kwadraty = [i**2 for i in range(21) if i % 2 == 0]
print(kwadraty)

# Przekształcenie danych
# Mając listę:
osoby = [("Anna", 18), ("Bartek", 22), ("Celina", 17), ("Dawid", 19)]
# Użyj list comprehension i lambdy, by uzyskać tylko pełnoletnich w postaci:
# [{'name': 'Bartek', 'age': 22}, {'name': 'Dawid', 'age': 19}]
compra = lambda lista : [{'name': imie, 'age': wiek} for imie, wiek in lista if wiek >= 18]
print(compra(osoby))

# Suma długości słów
# Użyj map() i reduce(), aby obliczyć łączną długość słów w liście
words = ["Python", "Lambda", "Comprehension"]
dlugosc = lambda lista : reduce(lambda x, y: x + y, map(lambda w: len(w), lista))
print(dlugosc(words))

#! Exercises part 2 - after brake
#Zad 1 Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
output = [i for i in numbers if i <= 0]
print(output)

#Zad 2 Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''
output [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

output = [inner for outer in list_of_lists for inner in outer]
print(output)

#Zad 3 
output = [(i,1,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
for i in output:
    print(i)

#Zad 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[first.upper(), first.upper()[:3], last.upper()] for country in countries for first,last in country]
print(output) 

#Zad 5 
output = [{'country': first, 'city': last} for country in countries for first,last in country]
for i in output:
    print(i)

#Zad 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [f'{Name} {Surname}' for person in names for Name, Surname in person]
print(output)

#Zad 7 Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1,x2,y1,y2:(y2 - y1)/(x2 - x1)
print(slope(4,8,5,7))

a = [1,2,3,4,5]
print(a[1:3])