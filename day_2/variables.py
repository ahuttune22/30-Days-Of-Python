# Day 2: 30 Days of python programming

import math

first_name = "Matti"
last_name = "Meikäläinen"
full_name = "Matti Meikäläinen"
country = "Finland"
city = "Helsinki"
age = 23
year = 2026
is_married = False
is_true = True
is_light_on = False

first_name, last_name, country, age, is_married = (
    "Matti",
    "Meikäläinen",
    "Finland",
    23,
    False,
)

variables = {
    "first_name": first_name,
    "last_name": last_name,
    "full_name": full_name,
    "country": country,
    "city": city,
    "age": age,
    "year": year,
    "is_married": is_married,
    "is_true": is_true,
    "is_light_on": is_light_on,
}

for name, value in variables.items():
    print(name, type(value))


print(len(first_name))

length_of_first_name = len(first_name)
length_of_last_name = len(last_name)

if length_of_first_name < length_of_last_name:
    print(
        "The length of your first name is shorter than your last name.\n"
        f"First name is {length_of_first_name} characters long.\n"
        f"Last name is {length_of_last_name} characters long."
    )
elif length_of_first_name > length_of_last_name:
    print(
        "The length of your first name is longer than your last name.\n"
        f"First name is {length_of_first_name} characters long\n"
        f"Last name is {length_of_last_name} characters long."
    )
elif length_of_first_name == length_of_last_name:
    print(
        "The length of your first and last name are the same.\n"
        f"Both are {length_of_first_name} characters long."
    )

num_one = 5
num_two = 4

total = num_one + num_two
print(total)

diff = num_one - num_two
print(diff)

product = num_one * num_two
print(product)

division = num_one / num_two
print(division)

remainder = num_two % num_one
print(remainder)

exp = math.pow(num_one, num_two)  # Or num_one ** num_two?
print(exp)

floor_division = num_one // num_two
print(floor_division)

radius = 30

area_of_circle = math.pi * radius**2
print(area_of_circle)

circum_of_circle = 2 * math.pi * radius
print(circum_of_circle)

input_radius = float(input("Enter the radius of a circle to calculate it's area: "))

user_area_of_circle = math.pi * input_radius**2
print(user_area_of_circle)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
country = input("Enter your country of birth: ")

print(
    f"Hello {first_name} {last_name}! \n"
    f"I see that you are {age} years old and from {country}."
)


help("keywords")
