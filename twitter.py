my_string = input("Input: ")


print ("Output: ",end= "")
for tweet in my_string:
   if not tweet in  ["a","e","i","o","u","A","E","I","O","U"]:
    print(tweet, end= "")
   