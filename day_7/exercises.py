# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Twitter")

it_companies.update(["Nokia", "Oura", "Polar"])

it_companies.remove("Facebook")
# Unlike set.remove(), the discard() method does not raise an exception
# #when an element is missing from the set.

print(it_companies)

a_union_b = A.union(B)  # A OR B
print(a_union_b)

a_intersection_b = A.intersection(B)
print(a_intersection_b)  # A AND B

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
print(A.union(B))
print(B.union(A))

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del A
del B

# Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set,
# which one is bigger?
print(len(age))
print(len(set(age)))


# Explain the difference between the following data types: string, list, tuple and set

# I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence?
# Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
print(len(set(words)))
