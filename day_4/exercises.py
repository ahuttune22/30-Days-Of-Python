sentence1 = " ".join(["Thirty", "Days", "Of", "Python"])
print(sentence1)

sentence2 = " ".join(["Coding", "For", "All"])
print(sentence2)

company = "Coding For All"
print(company)

print(len(company))

print(company.upper())
print(company.lower())

print(company.capitalize().title().swapcase())

print(company[7:])

print("Coding" in company)

print(company.replace("Coding", "Python"))

print(company.split())

actual_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(actual_companies.split(","))

print(company[0])
print(company[-1])
print(company[10])


acronym1 = "PFE"  # Python For Everyone
acronym2 = "CFA"  # Coding For All

print(company.index("C"))
print(company.index("F"))
print(company.rfind("l"))

sentence3 = "You cannot end a sentence with because because because is a conjunction"

print(sentence3.find("because"))
print(sentence3.rfind("because"))

result = sentence3.replace("because because because", "")
print(result)

if company.startswith("Coding"):
    print("Yes it does!")
else:
    print("No.")

if company.endswith("Coding"):
    print("Yes it does!")
else:
    print("No.")

sentence4 = "   Coding For All      "

print(sentence4.strip(" "))

option1 = "30DaysOfPython"
option2 = "thirty_days_of_python"

if option1.isidentifier():
    print(f"{option1} is identifier")
elif option2.isidentifier():
    print(f"{option2} is identifier")
else:
    print("None of them are")

python_libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]

libraries_result = "# ".join(python_libraries)

print(libraries_result)

print("I am enjoying this challenge. \nI just wonder what is next.")

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius**2

# method 1:
print(f"The area of a circle with radius {radius:.0f} is {area:.0f} m².")
# method 2:
print("The area of a circle with radius {:.0f} is {:.0f} m².".format(radius, area))
# method 3:
print("The area of a circle with radius %d is %d m²." % (radius, area))

a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))  #
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a**b))
