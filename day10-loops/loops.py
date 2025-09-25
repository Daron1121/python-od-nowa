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
#* Data With Baara

for item in (1,2,3,4,5):
    print(f'round {item}')

for seven in range(11):
    print(f'7 x {seven} = {7 * seven}')

days = ['Mon', 'Sun' , 'Wed' , 'Tue']
weekends = ['Sat', 'Sun']
for day in days:
    if day in weekends:
        continue
    print(f"Workday: {day}")
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

# Ex 4
for x in range(8):
    print(8 * '# ')
    if x == '# ':
        for y in x:
            print(y)
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
#Ex 1
sum = 0
for numbers1 in range(101):
    sum = sum + numbers1
print(f'The sum of all numbers is {sum}.')

#Ex 2
SumOfOdd = 0
SumOfEven = 0
for numbers1 in range(101):
    if numbers1 % 2 == 0:
        SumOfEven = SumOfEven + numbers1
    else:
        SumOfOdd = SumOfOdd + numbers1
print(f'The sum of all evens is {SumOfEven}. And the sum of all odds is {SumOfOdd}.')

#* Exercises: Level 3
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
for iter in countries:
    if 'land' in iter:
        print(iter)

#todo Ex 2
fruits = ['banana', 'orange', 'mango', 'lemon']
n = len(fruits) # 4
for i in range(n // 2): 
    fruits[i], fruits[n - 1 - i] = fruits[n - 1 - i], fruits[i]
    print(fruits)

#todo Ex 3
import sys, os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from countries_data import nowalista

# i: What are the total number of languages in the data
languages1 = []
for iter in nowalista:
    languages1 = languages1 + iter['languages']
print(f"Number of languages in file: {len(set(languages1))}")
# ii: Find the ten most spoken languages from the data
liczenie = {}
for lang in languages1:
    if lang not in liczenie:
        liczenie[lang] = 1
    else:
        liczenie[lang] += 1
top_ten = sorted(liczenie.items(), key=lambda x: x[1], reverse=True)[:10]
print(top_ten)
