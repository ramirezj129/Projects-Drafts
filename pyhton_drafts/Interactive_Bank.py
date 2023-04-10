class Bank_Acccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposits(self, amount1):
        self.balance += amount1

    def withdrawls(self, amount2):
        if amount2 < self.balance:
            self.balance -= amount2
        else:
            print("Account balance too low")
            exit(1)

    def disp_checking(self):
        print("Your current balance is: ", self.balance)


def main():
    bank_acc = Bank_Acccount()

    while True:
        answer = input(
            "Would you like to Deposit, Withdraw, or Exit (D/W/EXIT): "
        ).lower()

        if answer == "d":
            amount1 = int(input("Enter the amount: "))
            bank_acc.deposits(amount1)
            bank_acc.disp_checking()

        elif answer == "w":
            amount2 = int(input("Enter the amount you wish to withdraw: "))
            bank_acc.withdrawls(amount2)
            bank_acc.disp_checking()

        elif answer == "exit":
            print("Have a Good day!")
            break
        else:
            print("Enter correct input")
            continue


if __name__ == "__main__":
    main()
