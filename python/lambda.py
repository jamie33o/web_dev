people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Slytherin"},
    {"name": "Draco", "house": "Ravencla"}
]
#lambda function
people.sort(key=lambda person: person["name"])

print(people)