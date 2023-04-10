students = [
    {"Name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
    {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
    {"Name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russel"},
    {"Name": "Draco", "House": "Slytherine", "Patronus": None},
]

for student in students:
    print(student["Name"], student["House"], student["Patronus"], sep=", ")
