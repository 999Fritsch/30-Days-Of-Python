import math

# Arithmetic Operations in Python
# Integers
"""
print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
"""

def triangle_area():
    
    base = int(input("Enter base: "))
    height = int(input("Enter height: "))
    area = 0.5*(base*height)
    print("The area of the triangle is:", area)

def triangle_perimeter():
    
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
    print("The perimeter of the triangle is", sum([a,b,c]))

def rectangle():
    
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    
    area = length * width
    perimeter = 2 * (length + width)
    
    print(f"The area of the rectangle is {area} and the perimeter {perimeter}")

def circle():
    
    radius = int(input("Enter the radius: "))
    
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    
    print(f"The area of the circle is {area} and the circumference is {circumference}")

def function_1(x: int) -> int:
    return 2 * x -2

class Linear_function():
    
    def __init__(self, slope, y_intercept) -> None:
        
        self.slope = slope
        self.y_intercept = y_intercept
        self.function = lambda x: self.slope * x + self.y_intercept
    
    def __call__(self, x) -> float:
        return self.function(x)
    
    def calculate_slope(self, x1=5, x2=7) -> float:
        
        y1 = self.function(x1)
        y2 = self.function(x2)
        
        return (y2 - y1) / (x2 - x1)
    
    def calculate_x_intercept(self) -> float:
        # y = m * x + b
        # x = (y - b) / m
        
        return (0 - self.y_intercept) / self.slope
    
    def calculate_y_intercept(self, x=5) -> float:
        # y = m * x + b
        # b = y - m * x
        y = self.function(x)
        return y - self.slope * x


def calculate_slope(f):
    
    x1 = 5
    x2 = 7
    
    y1 = f(x1)
    y2 = f(x2)
    
    slope = (y2 - y1) / (x2 - x1)
    
    return slope

def calculate_slope_of_two_points(p1:tuple, p2:tuple)


if __name__ == "__main__":
    
    # age = 24
    # my_height = 1.83
    # complex_number = 1j
    
    my_function = Linear_function(slope=2, y_intercept=-2)
    
    slope = my_function.calculate_slope()
    print(slope)
    
    x_intercept = my_function.calculate_x_intercept()
    print(x_intercept)
    
    y_intercept = my_function.calculate_y_intercept()
    print(y_intercept)
    