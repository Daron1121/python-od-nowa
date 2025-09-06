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
'''

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

print(len('dragon'))
print(len('python'))
print(len('dragon') != len('python'))