empty_tuple = ()

brothers = ("Masa", "Joni", "Joona")
sisters = ("Anni", "Marjatta")
siblings = brothers + sisters

print(f"You have {len(siblings)} siblings")

siblings = list(siblings)

siblings.extend(["Matti", "Kerttu"])

family_members = siblings

print(family_members)

*siblings, mother, father = family_members
parents = mother + father
print(parents)
print(siblings)

fruits = ("Banana", "Apple", "Mango")
vegetables = ("Broccoli", "Carrot", "Paprika")
animal_products = ("Beef", "Chicken", "Fish", "Cow")

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

middle = len(food_stuff_lt) // 2

if len(food_stuff_lt) % 2 != 0:
    middle_item = food_stuff_lt[middle]
else:
    middle_item = food_stuff_lt[middle - 1 : middle + 1]

print(middle_item)

first_three_items = food_stuff_lt[:3]

last_three_items = food_stuff_lt[-3:]

print(first_three_items)
print(last_three_items)

del food_stuff_tp

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

is_estonia_nordic = "Estonia" in nordic_countries

is_iceland_nordic = "Iceland" in nordic_countries

print(is_estonia_nordic)
print(is_iceland_nordic)
