amountdue = 50
while amountdue > 0:
    print("Amount Due: ", amountdue)
    user_coin = int(input("Insert Coin: "))
    if user_coin in [25, 10, 5]:
        amountdue -= user_coin
    elif user_coin != [25, 10, 5]:
        print("Not accepted")
    continue

change = abs(amountdue)
print("Change Owed: ", change)
