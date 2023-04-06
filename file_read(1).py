
names=[]
with open("names.txt") as file: 
    for line in file:
        names.append(line.rstrip())

for names in sorted(names):
    print(f"Hello, {names}")
   

   