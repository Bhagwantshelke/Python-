class ATM:
    def __init__(self,balance, pin, card_number):
        self.balance=balance
        self.pin=pin
        self.card_number=card_number
    def get_details(self):
        print("\n ----------ACCOUNT DETAILS----------")
        print("ACCOUNT BALANCE: ",self.balance)
        print("PIN: ",self.pin)
        print("CARD NUMBER: ",self.card_number)

    def deposit(self, amount):
        self. amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Rs.", self.balance)
        print()
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Rs.{self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Nu.{amount} withdrawal successful!")
            print("Current account balance: Nu.", self.balance)
            print()

    def update_pin(self):
        pin = int(input("Enter Current Pin: "))
        new_pin = int(input("Enter new Pin: "))
        pin = new_pin

    def get_balance(self):
        print("Available balance: Rs.", self.balance)
        print()

    def transaction(self):
        print("""
              1. Account Detail
              2. Check Balance
              3. Deposit
              4. Withdraw
          """)
        while True:
            option = int(input("Enter 1, 2, 3, 4 :"))
            if option == 1:
                ATM.get_details()
            elif option == 2:
                ATM.get_balance()
            elif option == 3:
                amount = int(input("How much you want to deposit(Rs.):"))
                ATM.deposit(amount)
            elif option == 4:
                amount = int(input("How much you want to withdraw(Rs.):"))
                ATM.withdraw(amount)




atm1 = ATM(5000,1234,101)
atm2 = ATM(4000,4567,102)
atm3 = ATM(8000,6011,103)
atm4 = ATM(9000,5012,104)
atm4.transaction()