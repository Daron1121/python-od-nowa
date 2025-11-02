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

#* Exercises: Level 2
#Ex 4 Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
with open('./data/email_exchanges_big.txt', 'r', encoding='utf-8') as f:
    emails = re.findall(r'From:\s*([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})', f.read())
    print(emails)

#Ex 5 Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
def find_most_common_words(plik_lub_tekst, ile):
    try:
        with open(plik_lub_tekst, 'r', encoding='utf-8') as f:
            text = f.read().lower()
    except FileNotFoundError:
        text = plik_lub_tekst
    
    words = re.findall(r'\b\w+\b',text)

    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    sorted_arr = sorted(word_count.items(), key= lambda x: x[1], reverse=True)
    return sorted_arr[:ile]

print(find_most_common_words('ale nie wiem co dac ale dam to', 10))
# Ex 6 Use the function, find_most_frequent_words to find: 

# a) The ten most frequent words used in Obama's speech 
print(find_most_common_words('./data/obama_speech.txt', 10))

# b) The ten most frequent words used in Michelle's speech 
print(find_most_common_words('./data/michelle_obama_speech.txt', 10))

# c) The ten most frequent words used in Trump's speech 
print(find_most_common_words('./data/donald_speech.txt', 10))

# d) The ten most frequent words used in Melina's speech
print(find_most_common_words('./data/melina_trump_speech.txt', 10))


# Ex 7 Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
def check_simmilarity(tekst):
    def clean_text(tekst):
        with open(tekst, 'r', encoding='utf-8') as f:
            f = f.read().lower()
            f = re.sub(r'[^a-z\s]', '', f)
            f = re.sub(r'\s+', ' ', f).strip()
            return f

    cleaned = clean_text(tekst)

    def remove_support_words(tekst):
        stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
        nowy_tekst = ''
        for word in tekst.split():
            if word not in stop_words:
                nowy_tekst += f'{word} '
        return nowy_tekst.strip()

    stop_words_removed = remove_support_words(cleaned)



    return stop_words_removed

tekst1 = check_simmilarity('./data/melina_trump_speech.txt')
print(tekst1)
print(60*'-')
tekst2 = check_simmilarity('./data/michelle_obama_speech.txt')
print(tekst2)


# Ex 8  Find the 10 most repeated words in the romeo_and_juliet.txt
print(find_most_common_words('./data/romeo_and_juliet.txt', 10))

# Ex 9  Read the hacker news csv file and find out: 
def count_lines(text, co_szukac ,czego_nie=None):
    with open(text, 'r', encoding='utf-8') as f:
        licznik = 0
        for line in f:
            if co_szukac in line.lower() and (czego_nie is None or czego_nie not in line.lower()):
                licznik += 1
        return licznik
# a) Count the number of lines containing python or Python 
print(count_lines('./data/hacker_news.csv', 'python'))
# b) Count the number lines containing JavaScript, javascript or Javascript 
print(count_lines('./data/hacker_news.csv', 'javascript'))
# c) Count the number lines containing Java and not JavaScript
print(count_lines('./data/hacker_news.csv', 'java', 'javascript'))