import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "data"))
from countries import countries

empty_list = []

six_item_list = [1, 2, 3, 4, 5, 6]

print(len(six_item_list))

print(six_item_list[::2])

mixed_data_types = ["Masa", 23, 176, False, "Maakotkantie"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies)

print(len(it_companies))

first = it_companies[0]
middle = it_companies[len(it_companies) // 2]
last = it_companies[-1]

print(first, middle, last)

it_companies[0] = "Nokia"
print(it_companies)

it_companies.append("Oura")
print(it_companies)

middle_pos = len(it_companies) // 2

it_companies.insert(middle_pos, "Supercell")
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

print("#;  ".join(it_companies))

company = input("Enter a company to check if they are in our list: ")

company_exists = company in it_companies

if company_exists:
    print(f"{company} does exist in our list: {it_companies}!")

else:
    print(f"{company} does NOT exist in our list: {it_companies}!")

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

sliced_it_companies = it_companies[3:]
print(sliced_it_companies)

back_sliced_it_companies = it_companies[:-3]
print(back_sliced_it_companies)

middle2 = it_companies[len(it_companies) // 2]
it_companies.remove(middle2)
print(it_companies)

first = it_companies.pop(0)
print(it_companies)

last = it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]

joined = front_end + back_end

full_stack = joined.copy()

redux_pos = full_stack.index("Redux")
full_stack.insert(redux_pos + 1, "SQL")
full_stack.insert(redux_pos + 1, "Python")

print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

min_age = min(ages)
max_age = max(ages)

ages.append(min_age)
ages.append(max_age)

ages.sort()

size = len(ages)

if size % 2 == 0:
    median = (ages[size // 2 - 1] + ages[size // 2]) / 2
else:
    median = ages[size // 2]

average = sum(ages) / len(ages)

range_of_ages = max(ages) - min(ages)
print(range_of_ages)

min_diff = abs(min(ages) - average)
max_diff = abs(max(ages) - average)


print("Sorted:", ages)
print("Min, Max:", min_age, max_age)
print("Median:", median)
print("Average:", average)
print("Range:", range_of_ages)
print("Min diff, Max diff:", min_diff, max_diff)

size = len(countries)

mid = size // 2

if size % 2 == 0:
    middle = countries[mid - 1 : mid + 1]
else:
    middle = countries[mid : mid + 1]

half = size // 2

if size % 2 == 0:
    first_half = countries[:half]
    second_half = countries[half:]
else:
    first_half = countries[: half + 1]
    second_half = countries[half + 1 :]

countries2 = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
first, second, third, *scandic_countries = countries2

print(first, second, third)
print(scandic_countries)
