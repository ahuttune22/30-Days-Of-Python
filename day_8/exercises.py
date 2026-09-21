dog = {}

dog.update(
    {"name": "Mortti", "color": "Brown", "breed": "Labrador", "legs": 4, "age": 5}
)

print(dog)

student = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "gender": "woman",
    "age": 25,
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "country": "Finland",
    "city": "Helsinki",
    "address": {"street": "Space street", "zipcode": "02210"},
}

print(len(student))

student_skills = student.get("skills")
print(type(student_skills))
print(student_skills)

student["skills"].append("HTML")
print(student_skills)

keys = student.keys()
values = student.values()

print(keys, "\n", values)

print(student.items())

student.popitem()
print(student)

del dog
