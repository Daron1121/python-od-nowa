import requests 
import json

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page

print(50*'-')
url = "https://restcountries.com/v3.1/all?fields=name,capital,region,population"

response = requests.get(url)
print(response.status_code)
if response.status_code == 200:
    countries = response.json()
    print(json.dumps(countries[:1], indent=2, ensure_ascii=False))
else:
    print(response.text)



#* Exercises 
# Ex 1 Read this url and find the 10 most frequent words.
romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(romeo_and_juliet)
print(response.status_code) # Code 404 - no file to fetch


import statistics
# Ex 2 Read the cats API and find :
cats_api = 'https://api.thecatapi.com/v1/breeds' 
# the min, max, mean, median, standard deviation of cats' weight in metric units.
cats = requests.get(cats_api)
kitten_info = cats.json()
information = []
for cat in kitten_info:
    information.append(cat['weight']['metric'])


def for_cats(to_iterate):
    nowe = []
    for met in to_iterate:
        met = met.split(" - ")
        liczby = [float(y) for y in met]
        srednia = sum(liczby)/len(liczby)
        nowe.append(srednia)
    print(min(nowe))
    print(max(nowe))
    print(statistics.mean(nowe))
    print(statistics.median(nowe))
    print(statistics.stdev(nowe))
# the min, max, mean, median, standard deviation of cats' weight in metric units.
cats = requests.get(cats_api)
kitten_info = cats.json()
information = []
for cat in kitten_info:
    information.append(cat['weight']['metric'])
print(for_cats(information))

print(50*'-')
# the min, max, mean, median, standard deviation of cats' lifespan in years.
information = []
for cat in kitten_info:
    information.append(cat['life_span'])
print(for_cats(information))


# Create a frequency table of country and breed of cats
def frequency(of_what):
    information = []
    for cat in kitten_info:
        information.append(cat[of_what])
    freq = {}
    for info in information:
        if info in freq:
            freq[info] += 1
        else:
            freq[info] = 1
    return freq
print(frequency('origin'))
print(frequency('name'))


# Ex 3 Read the countries API and find
url = "https://restcountries.com/v3.1/all?fields=name,capital,region,population,languages"
response = requests.get(url)
countries = response.json()
print(json.dumps(countries, indent=2, ensure_ascii=False))

#  Pomocnicza funkcja
def get_info(field):
    info = {}
    for country in countries:
        name = country["name"]["common"]
        value = country.get(field, None)
        info[name] = value
    return info

def find_it(smth):
    info = get_info(smth)
    if smth == "languages":
        # traktuj to jako języki
        lang_count = {}
        for langs in info.values():
            if isinstance(langs, dict):
                for lang in langs.values():
                    if lang in lang_count:
                        lang_count[lang] += 1
                    else:
                        lang_count[lang] = 1
        sorted_arr = sorted(lang_count.items(), key= lambda x : x[1], reverse=True)
        return sorted_arr[:10]
    elif smth == "population":
        # traktuj to jako liczby (np. populacja)
        sorted_arr = sorted(info.items(), key= lambda x : x[1], reverse=True)
        return sorted_arr[:10]
    else: 
        pass


# the 10 most populated
print(find_it('population'))

# the 10 most spoken languages
print(find_it('languages'))

# the total number of languages in the countries API
def lang_count(smth):
    info = get_info(smth)
    unique_langs = set()
    for langs in info.values():
        for lang in langs.values():
            unique_langs.add(lang)
    return f'Total number of unique countries in API: {len(unique_langs)}'
print(lang_count('languages')) 


# Ex 4 UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4