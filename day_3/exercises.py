import math
import random

age = 20
height = 1.81
complex_num = 1 + 1j

# Exercise 4
while True:
    try:
        triangle_base = float(input("Enter base: "))
        triangle_height = float(input("Enter height: "))

    except ValueError:
        print("Enter a valid number!")
        continue

    if triangle_base <= 0 or triangle_height <= 0:
        print("Neither length can't be negative or zero.")

    else:
        triangle_area = (1 / 2 * triangle_base) * triangle_height
        break


print(f"The area of the triangle is {triangle_area:.3f}")

# Exercise 5

print("*********************************")
print("  Triangle perimeter calculator  ")
print("*********************************")

while True:
    while True:
        try:
            side_a = float(input("Enter side a: "))
            side_b = float(input("Enter side b: "))
            side_c = float(input("Enter side c: "))

        except ValueError:
            print("Enter a valid number!")
            continue

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            print("No length can't be negative or zero.")

        else:
            triangle_perimeter = side_a + side_b + side_c
            break

    print(f"The perimeter of the triangle is {triangle_perimeter:.3f}")

    again = input("Calculate another triangle? (y/n): ").lower()
    if again != "y":
        break

# Exercise 8
m1 = 2  # coefficient of x -> slope
b = -2  # constant term -> y-intercept

x_intercept = -b / m1
y_intercept = b

print(f"Slope: {m1}")
print(f"x-intercept: {x_intercept}")
print(f"y-intercept: {y_intercept}")

# Exercise 9

x1, y1 = 2, 2
x2, y2 = 6, 10

m2 = (y2 - y1) / (x2 - x1)

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"Slope: {m2}")
print(f" Euclidean distance: {distance}")

# Exercise 10

if m2 > m1:
    diff = m2 - m1
    print(f"Slope 2: {m2} is steeper than slope 1: {m1}. The difference is {diff} ")

elif m2 < m1:
    diff = m1 - m2
    print(f"Slope 1: {m1} is steeper than slope 2: {m2}. The difference is {diff} ")

elif m2 == m1:
    diff = m1 - m2
    print(f"Slope 1 and slope 2 are equal. The difference is {diff} ")

# Exercise 11

# Exercise 11
for x in range(-6, 7):
    y = x**2 + 6 * x + 9
    print(f"x = {x}: y = {y}")

# Exercise 12

word1 = "python"
word2 = "dragon"
check = "on"

boolean_result = len(word1) != len(word2)
print(boolean_result)

# Exercise 13

if check in word1 and check in word2:
    print(f"'{check}' is in words {word1} and {word2}")

# Exercise 14

print("jargon" in "I hope this course is not full of jargon.")

# Exercise 16
print(str(float(len("python"))))

# Exercise 17

min = 1
max = 100
random_num = random.randint(min, max)
print(f"Your random number in range ({min}-{max}) is {random_num} ")
if random_num % 2 == 0:
    print(f"{random_num} is even!")

else:
    print(f"{random_num} is odd!")

# Exercise 18

print(7 // 3 == int(2.7))

# Exercise 19

print(type("10") == type(10))

# Exercise 20

print(int(float("9.8")) == 10)  # To convert a decimal string to an int,
# you have to go through float() first, then int():
# int('9.8') truncated is 9

# Exercise 21

while True:
    while True:
        try:
            hours = float(input("Enter hours: "))
            rate = float(input("Enter rate per hour: $"))
        except ValueError:
            print("Enter a valid number! ")
            continue

        if rate <= 0 or hours <= 0:
            print("Neither value should be zero!")

        else:
            weekly_earn = hours * rate
            break

    print(f"Your weekly earning is ${weekly_earn}")

    again = input("Calculate again? (y/n): ").lower()
    if again != "y":
        break
print("Goodbye!")

# Exercise 22

while True:
    while True:
        try:
            years = int(float(input("Enter number of years you have lived: ")))
        except ValueError:
            print("Enter a valid number! ")
            continue

        if years <= 0:
            print("That value should not be negative or zero!")

        else:
            seconds = years * 365 * 24 * 60 * 60
            break

    print(f"You have lived for {seconds:,.0f} seconds.")

    again = input("Calculate again? (y/n): ").lower()
    if again != "y":
        break
print("Goodbye!")

# Exercise 23

for i in range(1, 6):
    print(i, end=" ")
    for j in range(0, 4):
        print(i**j, end=" ")
    print()
