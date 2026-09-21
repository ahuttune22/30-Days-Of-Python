while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Enter a whole number!")

diff = 18 - age

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {diff} years to learn to drive.")

my_age = 22
your_age = int(input("Enter your age: "))

if my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
        print("I am one year older than you")
    else:
        print(f"I am {difference} years older than you")

elif my_age < your_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are one year older than me")
    else:
        print(f"You are {difference} years older than me")

else:
    print("You are the same age as me")

while True:
    try:
        value1 = int(input("Enter number one: "))
        value2 = int(input("Enter number two: "))
        break
    except ValueError:
        print("Enter a whole number!")

if value1 > value2:
    print(f"{value1} is greater than {value2}")

elif value1 < value2:
    print(f"{value1} is smaller than {value2}")

else:
    print(f"{value1} is equal to {value2}")

while True:
    try:
        score = int(input("Enter the student's score: "))
        if 0 <= score <= 100:
            break
        print("Enter a score between 0 and 100!")
    except ValueError:
        print("Enter a whole number!")

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

month = input("Enter a month: ").strip().capitalize()

if month in ("September", "October", "November"):
    season = "Autumn"
elif month in ("December", "January", "February"):
    season = "Winter"
elif month in ("March", "April", "May"):
    season = "Spring"
elif month in ("June", "July", "August"):
    season = "Summer"
else:
    season = "Unknown"

print(f"Season: {season}")

fruits = ["banana", "orange", "mango", "lemon"]
fruit = input("Enter a fruit: ").strip().lower()

if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(fruits)

person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {
        "street": "Space street",
        "zipcode": "02210",
    },
}

if "skills" in person:
    skills = person["skills"]
    print(f"Middle skill: {skills[len(skills) // 2]}")
    print(f"Has Python skill: {'Python' in skills}")

    if set(skills) == {"JavaScript", "React"}:
        print("He is a front end developer")
    elif {"Node", "Python", "MongoDB"}.issubset(skills):
        print("He is a backend developer")
    elif {"React", "Node", "MongoDB"}.issubset(skills):
        print("He is a fullstack developer")
    else:
        print("unknown title")

if person["is_married"] and person["country"] == "Finland":
    print(
        f"{person['first_name']} {person['last_name']} lives in "
        f"{person['country']}. He is married."
    )
