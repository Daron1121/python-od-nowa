countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print('Countries:', countries)
print('Number of countries:', len(countries))

'''
--------------------------------
Data with baara
--------------------------------
'''
# 1 - How to create a list
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

matrix = [['a', 'b', 'c'], ['d', 'e', 'f']]
print(matrix)

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