import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from data.countries import countries

for i in range(11):
    print(i)

number = 0
while number < 11:
    print(number)
    number += 1

for i in range(7):
    print("#" * (i + 1))

for i in range(8):
    for j in range(8):
        print(" # ", end="")
    print()

for i in range(11):
    print(f"{i} x {i} = {i * i}")
print()

programming = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for lang in programming:
    print(lang)

for i in range(101):
    if i % 2 == 0:
        print(i)

for i in range(101):
    if i % 2 != 0:
        print(i)
sum = 0
for i in range(101):
    sum += i
print(f"The sum of all numbers from 0 to 100 is: {sum}")

sum_evens = 0

for i in range(0, 101, 2):
    sum_evens += i
print(f"The sum of all even numbers from 0 to 100 is: {sum_evens}")

sum_odds = 0
for j in range(1, 101, 2):
    sum_odds += j
print(f"The sum of all odd numbers from 0 to 100 is: {sum_odds}")


land_countries = []
for country in countries:
    if "land" in country.lower():
        land_countries.append(country)

print(land_countries)

fruits = ["banana", "orange", "mango", "lemon"]
reversed_fruits = []
for index in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[index])
print(reversed_fruits)

countries_data_path = Path(__file__).resolve().parents[1] / "data" / "countries-data.py"
with countries_data_path.open(encoding="utf-8") as data_file:
    countries_data = json.load(data_file)

language_counts = Counter(
    language for country in countries_data for language in country["languages"]
)
print(f"Total number of languages: {len(language_counts)}")
print("Ten most spoken languages:")
for language, country_count in language_counts.most_common(10):
    print(f"{language}: {country_count} countries")

most_populated_countries = sorted(
    countries_data, key=lambda country: country["population"], reverse=True
)[:10]
print("Ten most populated countries:")
for country in most_populated_countries:
    print(f"{country['name']}: {country['population']:,}")
