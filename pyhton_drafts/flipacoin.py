import random

guess = input("Heads or Tails: ")
try:
    print(random.choice(("Heads", "Tails\n")))
except:
    ValueError
