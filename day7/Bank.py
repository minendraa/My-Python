class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance
        self.__pin = "5678"
        print(f"Account created for {self.owner}")

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self._balance:
            print(f"Insufficient funds. Cannot withdraw ${amount}. Balance is ${self._balance}")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")

    # Public method to get balance (controlled access)
    def get_balance(self):
        print(f"Current balance for {self.owner}: ${self._balance}")
        # We can access the "private" attribute internally
        print(f"   (Pin : {self.__pin})")
        return self._balance

    def get_pin(self):
        print(f"Current pin for {self.owner}: ${self._balance}")
        if self.__pin == "5678":
            print(f"   (Now the pin is: {self.__pin})")
        return self.__pin

   
acc1=BankAccount("Minendra")

acc1.get_balance()
acc1.deposit(500)
acc1.withdraw(200)
acc1.withdraw(2000)

acc1.get_balance()
acc1.get_pin()
acc1.__pin="3456"
print((acc1.__pin))

print(id(acc1.__pin))
print(id(acc1._BankAccount__pin))
acc1.get_pin()

