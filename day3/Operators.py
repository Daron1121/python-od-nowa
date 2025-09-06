'''
age = 17
height = 182.5
v_store = 3j

# Script 1
height = int(input("Enter triangle hight "))
base = int(input("Enter triangle base "))
area = 0.5 * base * height
print("area: " + str(area))

# Script 2
a = int(input("Enter side a of tiangle "))
b = int(input("Enter side b of tiangle "))
c = int(input("Enter side c of tiangle "))
perimeter = a + b + c
print("perimeter:" + str(perimeter))

# Script 3
length = int(input("Enter rectangle length "))
width = int(input("Enter rectangle width "))

area = length * width
perimeter = 2 * (length + width)

print("area: " + str(area))
print("permiter: " + str(perimeter))

# Script 3
radius = int(input("Enter circle radius "))

area = radius*radius*3.14
circumference = 2 * 3.14 * radius

print("area: "+ str(area))
print("curicumference: "+ str(circumference))

# Script 4
a = 2
b = 1
c = 2
slope4 = -(a/b)

# y-intercept (x=0)
y_intercept = (0, -c / b)

# x-intercept (y=0 => ax + c = 0 => x = -c/a)
x_intercept = (-c / a, 0)

print("slope4: "+ str(slope4))
print("y_intercept: "+ str(y_intercept))
print("x_intercept: "+ str(x_intercept))


# Script 5
x1, y1 = 2, 2
x2, y2 = 6, 10
slope5 = (y2 -y1) / (x2- x1)
print("slope5: "+ str(slope5))

# Script 6 - 10
print(slope5 == slope4)
print(slope5 != slope4)
print(slope5 > slope4)
print(slope5 < slope4)
'''
# Script 6 - 12
print(len('dragon'))
print(len('python'))
print(len('dragon') != len('python'))

# Script 7 - 13
print('on' in "python")
print('on' in "dragon")

# Script 8 - 14
print("jargon" in "I hope this course is not full of jargon.")

# Script 9 - 16
print(float(len("python")))
print(str(len("python")))

# Script 10 - 17
def IsEven(x):
    if (x % 2) == 0:
        print('Even')
    else:
        print("Odd")
IsEven(5)

# Script 11 - 18
print((7 // 3) == int(2.7))
print(int(2.7))

# Script 12 - 19
print(type('10'))
print(type(10))
print(type(10) == type('10'))

# Script 13 - 20
print(int(float('9.8')))
print(int(float('9.8')) == 10)

# Script 14 - 21
earn = input("How much u Earn?")
hours = input("How many hours you work?")
print("Your weekly earning is " + str(int(earn) * int(hours)))

years = input("how many years your lived:")
y_to_sec = int(years) * 365 * 24 * 60 * 60
print(y_to_sec)

print("n  1  n  n^2  n^3")
for n in range(1, 6):
    print(n, 1, n, n**2, n**3)