import random

def generate_random_number_easy():
    return random.randint(1, 50)

def generate_random_number_medium():
    return random.randint(1, 100)

def generate_random_number_hard():
    return random.randint(1, 500)

def gra():
    licznik_prob = 1
    user = None
    while user != generowana:
        try:
            user = int(input('Twoja Odpowiedz:'))
            if user == generowana:
                print(f'🎉 Gratulacje!!!! Wygrałeś w {licznik_prob} próbach!')
                break
            elif user < generowana:
                print('Liczba jest wyższa!')
                print('Sprobuj ponownie!')
                licznik_prob = licznik_prob + 1
            elif user > generowana:
                print('Liczba jest niższa!')
                print('Sprobuj ponownie!')
                licznik_prob = licznik_prob + 1
        except ValueError:
            print('❌Niepoprawny Format Odpowiedzi')

print('Wybierz poziom trudnosci!')
poziom = input('1 - łatwy , 2 - średni , 3 - trudny')
if poziom == '1':
    generowana = generate_random_number_easy()
    x = 50
elif poziom == '2':
    generowana = generate_random_number_medium()
    x = 100
elif poziom == '3': 
    generowana = generate_random_number_hard()
    x = 500
print('Została wygenerowana randomowa liczba!')
print('Zgadnij liczbe od 0 do ' + str(x) + '!')

gra()
