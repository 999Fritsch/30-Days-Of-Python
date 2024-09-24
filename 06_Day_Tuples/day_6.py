empty_tuple = ()

sisters = ("Anna", "Marie")

brothers = ("Peter", "Tim")

siblings = sisters + brothers

print(len(siblings))

parents = ("Jürgen", "Lisa")

family = siblings + parents

print(family)

siblings = family[:4]

parents = family[4:6]

print(siblings)

print(parents)

fruits = ("Orange", "Apple", "Peach", "Mango")

vegetables = ("Tomato", "Potato", "Cucumber", "Onion", "Garlic")

animal_products = ("Honey", "Eggs", "Meat", "Leather")

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

food_stuff_lt = food_stuff_lt[:6] + food_stuff_lt[7:]

print(food_stuff_lt)

food_stuff_lt = food_stuff_lt[3:-3]

print(food_stuff_lt)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)

print("Iceland" in nordic_countries)