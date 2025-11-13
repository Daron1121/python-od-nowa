class Person:
    pass
p = Person()
print(Person)
print(p)

class Person:
    def __init__(self, firstname="Asabeneh", lastname="Yetayeh", age="200", country="Finland", city="Helsinki"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
print(p.person_info())

p2 = Person()
print(p2.person_info())

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)


class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)


print(80*'-')
# --------------------------------------------------------------
#* Exercises: Day 21
# --------------------------------------------------------------
#* Exercises: Level 1

# Ex 1 Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
class Statistics():
    def __init__(self, liczby):
        self.liczby = liczby
    def count(self):
        counting = 0
        for liczba in self.liczby:
            counting += 1
        return counting

    def get_sum(self):
        suma = 0
        for liczba in self.liczby:
            suma += liczba
        return suma

    def get_min(self):
        najmniejsza = self.liczby[0]
        for liczba in self.liczby:
            if liczba < najmniejsza:
                najmniejsza = liczba
        return najmniejsza

    def get_max(self):
        najwieksza = self.liczby[0]
        for liczba in self.liczby:
            if liczba > najwieksza:
                najwieksza = liczba
        return najwieksza
        
    def get_range(self):
        return max(self.liczby) - min(self.liczby)

    def mean(self):
        return self.get_sum() / self.count()

    def median(self):
        posortowane = sorted(self.liczby)
        n = self.count()
        if n % 2 != 0:
            return posortowane[n // 2]
        else:
            mid1 = posortowane[n // 2 - 1]
            mid2 = posortowane[n // 2]
            return (mid1 + mid2) / 2
 

    def mode(self):
        data = sorted(self.liczby)  
        freq = {}
        for liczba in data:
            freq[liczba] = freq.get(liczba, 0) + 1
        max_freq = max(freq.values())
        modes = [k for k, v in freq.items() if v == max_freq]
        return modes if len(modes) > 1 else modes[0]

    def std(self):
        mean = self.get_sum() / self.count()
        data = self.liczby
        differences = []
        for cos in data:
            differences.append((cos - mean)**2)
        return sum(differences) / len(differences)

    def var(self):
        mean = self.mean()
        data_points_sqared = []
        for every in self.liczby:
            data_points_sqared.append((every-mean)**2)
        suma = 0
        for every in data_points_sqared:
            suma += every
        return suma/len(self.liczby)

    def freq_dist(self):
        freq = {}
        for liczba in self.liczby:
            freq[liczba] = freq.get(liczba, 0) + 1
        freq_sorted = sorted([(count * 100 / len(self.liczby), liczba) for liczba, count in freq.items()], reverse=True)
        return freq_sorted   


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.get_sum()) # 744
print('Min: ', data.get_min()) # 24
print('Max: ', data.get_max()) # 38
print('Range: ', data.get_range()) # 14
print('Mean: ', data.mean()) # 29.76
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]



#* Exercises: Level 2

# Ex 2 Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.
class PersonAccount():
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        pass
    
    def total_expense(self):
        pass

    def account_info(self):
        pass

    def add_income(self):
        pass

    def add_expense(self):
        pass

    def account_balance(self):
        pass
