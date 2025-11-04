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
metrics = []
for cat in kitten_info:
    metrics.append(cat['weight']['metric'])
nowe = []
for met in metrics:
    met = met.split(" - ")
    liczby = [float(y) for y in met]
    srednia = sum(liczby)/len(liczby)
    nowe.append(srednia)
print(min(nowe))
print(max(nowe))
print(statistics.mean(nowe))
print(statistics.median(nowe))
print(statistics.stdev(nowe))

# the min, max, mean, median, standard deviation of cats' lifespan in years.

# Create a frequency table of country and breed of cats



# Ex 3 Read the countries API and find
# the 10 largest countries
# the 10 most spoken languages
# the total number of languages in the countries API



# Ex 4 UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4