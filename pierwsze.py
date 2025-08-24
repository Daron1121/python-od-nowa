import random

def generate_random_number(max_value):
    return random.randint(1, max_value)


def gra(generowana, x):
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
                print("------------------------------------------")
                licznik_prob = licznik_prob + 1
            elif user > generowana:
                print('Liczba jest niższa!')
                print('Sprobuj ponownie!')
                print("------------------------------------------")
                licznik_prob = licznik_prob + 1
        except ValueError:
            print('❌Niepoprawny Format Odpowiedzi')

print('Wybierz poziom trudnosci!')
poziom = input('1 - łatwy , 2 - średni , 3 - trudny')

trudnosc = {
    '1': 50,
    '2': 100,
    '3': 500
}


if poziom in trudnosc:
    x = trudnosc[poziom]
    generowana = generate_random_number(x)
    print("==========================================")
    print('Została wygenerowana randomowa liczba!')
    print('Zgadnij liczbe od 0 do ' + str(x) + '!')
    print("==========================================")
    gra(generowana, x)
else:
    print("❌ Niepoprawny wybór poziomu trudności!")