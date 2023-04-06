import csv

name = input("Enter a name: ")
home = input("Enter home: ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name, "home": home})