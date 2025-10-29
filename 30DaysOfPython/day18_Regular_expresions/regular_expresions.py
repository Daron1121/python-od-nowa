import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach


import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first

#! re.I - find all lowercase & uppercase characters!!!!

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']



match_replaced = re.sub('Python|python', 'JavaScript', txt)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, flags=re.I)
# match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I) #No flag returns error!!
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.



txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

#---------------------------------------------------------------
#* Splitting Text Using RegEx Split

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol


import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']


regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches) 

#---------------------------------------------------------------
#*Exercises
# Ex1 What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = {}
word_list = re.findall(r'\b\w+\b', paragraph.lower(), re.I)
for word in word_list:
    words_in = re.findall(rf'\b{word}\b', paragraph, re.I)
    words[word] = len(words_in)
print(words)

# Ex2
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."
numbers = re.findall(r'-?\d+', text)
numbers = [int(n) for n in numbers]
print(f"Distance between furthest particles: {max(numbers) - min(numbers)}")

#Exercises: Level 2
#Write a pattern which identifies if a string is a valid python variable
def is_valid_variable(Variable):
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    if re.match(pattern, Variable):
        return True
    else:
        return False
print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True


#Exercises: Level 3
#Clean the following text. After cleaning, count three most frequent words in the string.
import re
from collections import Counter

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(sent):
    to_sub = ['%', '@', '&', '$', '#', ';', '.', '?', '!']
    for l in to_sub:
        print(l)
        sent = re.sub(re.escape(l), '', sent)
    return sent
def most_frequent_words(text):
    # dzielimy tekst na słowa
    words = text.split()
    # liczymy częstość
    counter = Counter(words)
    return counter.most_common(3)


cleaned = clean_text(sentence)
print(cleaned)
print()

# zliczamy najczęstsze słowa
print(most_frequent_words(cleaned))

#! CHAT EXERCISES
# 🟢 Beginner Level (Basic Matching & Character Classes)
# 1. Match all email addresses in a string
# Task: Extract all valid email addresses.
# Example:
text = "Contact us at support@example.com or sales@shop.net"
matches = re.findall(r"\w+@\w+\.\w+", text)
print(matches)

# 2. Find all digits in a string
# Task: Return all digits from a mixed string.
# Example:
text = "My phone number is 415-555-2671"
# # Expected output: ['4', '1', '5', '5', '5', '5', '2', '6', '7', '1']
matches = re.findall(r'\d', text)
print(matches)

# 3. Match words starting with a capital letter
# Example:
text = "Alice and Bob went to New York City."
# Expected output: ['Alice', 'Bob', 'New', 'York', 'City']
matches = re.findall(r'\b[A-Z][a-z]+', text)
print(matches)

# 🟡 Intermediate Level (Groups, Quantifiers, Alternation)
# 4. Extract dates in DD/MM/YYYY format
# Example:
text = "Events: 12/10/2024, 03/05/2025 and 30/12/23"
# # Expected output: ['12/10/2024', '03/05/2025']
matches = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
print(matches)


# 5. Capture domain names from URLs

# Example:

text = "Visit https://www.google.com or http://openai.com."
# # Expected output: ['google', 'openai']
matches = re.findall(r'https?://(www\.)?(\w+)\.\w+', text)
domains = [m[1] for m in matches]
print(domains)

# 6. Find all repeated words
# Example:
text = "This is is a test test string"
# Expected output: ['is', 'test']

# Hint: Use backreferences like r'\b(\w+)\s+\1\b'


# 🔵 Advanced Level (Lookahead, Lookbehind, Complex Patterns)
# 7. Match numbers that are not followed by a percent sign
# Example:
text = "50%, 100, 75%, 200"
# # Expected output: ['100', '200']
matches = re.findall(r'\d\d+(?!%)', text)
print(matches)

# Hint: Use a negative lookahead (?!%)

# 8. Extract words inside quotes
# Example:
text = 'He said "hello" and then "goodbye".'
# # Expected output: ['hello', 'goodbye']
matches = re.findall(r'"(.*?)"', text)
print(matches)

# Hint: Use r'"(.*?)"'

# 9. Match valid IPv4 addresses
# Example:

text = "Valid: 192.168.0.1, Invalid: 999.999.1.1"
matches = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
def is_valid_ip(ip):
    parts = ip.split('.')
    return all(0 <= int(p) <= 255 for p in parts)

correct = [ip for ip in matches if is_valid_ip(ip)]
print(correct)

# Hint: Use something like
# r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
# and filter values <= 255.



# 🔴 Expert Level (Complex Validation, Nested Groups, Conditional Patterns)
# 10. Validate a password
# Requirements:
# At least 8 characters
# At least one uppercase, lowercase, digit, and special char
# Example:
# text = "MyPass123!"
# # Expected output: True









# Hint: Use a single regex with lookaheads:
# r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

# 11. Parse HTML tags (simple version)
# Example:
text = "<div><p>Hello</p></div>"
# # Expected output: ['div', 'p']
matches = re.findall(r'<(/?)(\w+)[^>]*>',text)
matches1 = []
for inner in matches:
    if inner[1] in matches1:
        continue
    else:
        matches1.append(inner[1])
print(matches1)









# Hint: Use r'<(/?)(\w+)[^>]*>' and groups.

# 12. Extract nested parentheses content (hard)
# Example:
# text = "f(x, g(y, z))"
# # Expected output: ['x, g(y, z)', 'y, z']


# Hint: Use recursive patterns (via regex module, not re):
# r'\((?:[^()]+|(?R))*\)'