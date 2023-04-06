Grocery = {}
i = 0

while(True):
 try: 
    item = input().lower()
    if item in Grocery:
     Grocery[item] +=1
    else:
      Grocery[item] = 1
     
 except EOFError:
    for key in sorted(Grocery.keys()):
      print(Grocery[key] , key.upper())
    break

