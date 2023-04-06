user_input = input("Input a fruit: ")


fruit  = {
            "apple":130,
            "orange":130,
            "banana":130,
            "guava":130,
            "tangarine":130,
            "peach":130,
            "grape":130,
            "chocolate":None

        }

        

for key in fruit:
    if key in user_input.lower():
        print("Calories: ", fruit[key])

