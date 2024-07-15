import math

def calculate_area(radius: float) -> float:
    return math.pi * radius**2


def calculate_circumference(radius: float) -> float:
    return 2 * math.pi * radius


def calculate_circle():
    radius = input("Radius: ")
    
    area_of_circle = calculate_area(float(radius))
    print('Area: ', round(area_of_circle,1))
    
    circum_of_circle = calculate_circumference(float(radius))
    print('Circumference: ', round(circum_of_circle, 1))


def get_user_info():
    
    first_name = input("first name: ")
    last_name = input("last name: ")
    country = input("country: ")
    age = input("age: ")    


if __name__ == "__main__":
    # calculate_circle()
    get_user_info()