#Exercises lvl 1
#Ex 1 - 5
empty_tuple = ()

brothers = ('maciek', 'grzegorz', 'adrian')
sisters = ('amelia', 'julia', 'nikola')

siblings = brothers + sisters
print(f"I have {len(siblings)} siblings")
siblings = list(siblings)
siblings.append('mother')
siblings.append('father')
family_members = tuple(siblings)
print(family_members)

#Exercises lvl 2
#Ex 1 - 7
siblings = family_members[:-2] 
parents = family_members[-2:] 
print(siblings)
print(parents)

fruits = ('apple','bannana','pineaple')
vegetables = ('tomato', 'celery')
animal = ('dog','cat')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(len(food_stuff_lt))

if len(food_stuff_lt) % 2 == 0:
    print(food_stuff_lt[len(food_stuff_lt) // 2 - 1 :len(food_stuff_lt) // 2 + 1])
else:
    print(food_stuff_lt[len(food_stuff_lt) // 2])

print(food_stuff_lt)
print(food_stuff_lt[:3] + food_stuff_lt[-3:])
del food_stuff_tp


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)