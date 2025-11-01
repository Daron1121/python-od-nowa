print('\nThis reads whole file')
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
txt = f.read()
print(txt)
f.close()

print('\nThis reads line')
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

print('\nThis reads all line and return as list')
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

# with open('./files/reading_file_example.txt', 'a') as f:
#     f.write('This text has to be appended at the end')

with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')


import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')


import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])


person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

person_json = json.dumps(person, indent=4)
print(type(person_json))
print(person_json)


person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)


import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are : {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines: {line_count}')

import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)

#--------------------------------------------------
#*Exercises
#--------------------------------------------------
# Exercises: Level 1
# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: 
def word_and_line_reader(file1) :
    with open(file1, 'r', encoding='utf-8') as f:
        count_of_words = 0
        count_of_lines = 0

        for line in f:
            count_of_lines += 1
            words = line.split()
            count_of_words += len(words)

        return f'There are {count_of_lines} lines and {count_of_words} words in this text'
            
# a) Read obama_speech.txt file and count number of lines and words
print(word_and_line_reader('./data/obama_speech.txt'))
# b) Read michelle_obama_speech.txt file and count number of lines and words 
print(word_and_line_reader('./data/michelle_obama_speech.txt'))
# c) Read donald_speech.txt file and count number of lines and words 
print(word_and_line_reader('./data/donald_speech.txt'))
# d) Read melina_trump_speech.txt file and count number of lines and words
print(word_and_line_reader('./data/melina_trump_speech.txt'))


#Ex 2
# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_languages(filename, nums):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)   # <-- konwersja z tekstu JSON do obiektu Python (lista/dict)

    languages = {}
    for country in data:
        for language in country['languages']:
            languages[language] = languages.get(language, 0) + 1
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:nums]
    

print(most_spoken_languages('./data/countries_data.json', 10))
print(most_spoken_languages('./data/countries_data.json', 3))

def most_populated_countries(filename, nums):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    info = []
    for dictionary in data:
        info.append({'country': dictionary['name'], 'population': dictionary['population']})
    sorted_countries = sorted(info, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:nums]
print(most_populated_countries('./data/countries_data.json', 10))