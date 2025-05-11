class BankAccount:
    def __init__ (self, name, account_num, opening_balance):
        self.name =name
        if len(str(account_num)) == 6:
            self.account_num = account_num  
        else:
            raise ValueError("Data must contain at 6 elements.")         
        self.balance = opening_balance
    def get_account_num(self):
        return self.account_num
    def get_name(self):
        return self.name
    def get_bal(self):
        return self.balance
    def withdraw(self, amount):
        initial_balance =self.balance  
        new_balance = int(initial_balance) - int(amount)
        if new_balance < 0:
            print("Fail, not enough money")
            pass
        else:
             self.balance = new_balance
    def deposit(self, amount):
        initial_balance =self.balance  
        new_balance = int(initial_balance) + int(amount)
        self.balance = new_balance        

dave=BankAccount("Dave Smith",111111,"680")
chris = BankAccount("Chris Citizen",111112,"3")
name = str(input("Username: "))
password = str(input("Password: "))
if name == "chris":
        choice_boring = str(input("Type 1 to add a deposit, 2 to withdraw and 3 to exit: "))
        amount = str(input("How much money would you like to add or remove (do not do a dollar sign just write the number as an int/float)"))
        if choice_boring == "1":
            chris.withdraw(amount)
            print(chris.get_bal())
        elif choice_boring == 2:
            chris.deposit(amount)
            print(chris.get_bal())
elif name == "dave":
    choice_boring = str(input("Type 1 to add a deposit, 2 to withdraw and 3 to exit: "))
    amount = str(input("How much money would you like to add or remove (do not do a dollar sign just write the number as an int/float)"))
    if choice_boring == "1":
        dave.withdraw(amount)
        print(dave.get_bal())
    elif choice_boring == 2:
        dave.deposit(amount)
        print(dave.get_bal())
else:
    print("No account")
