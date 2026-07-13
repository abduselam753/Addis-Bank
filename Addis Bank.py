class Account:
    def __init__ (self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance    

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance < amount:
            raise ValueError("Insufficient Fund")    
        self.__balance -= amount


Abebech = Account("Abebech", 100001 , 0)
Marta = Account("Marta", 100002, 0)

Marta.deposit(36767.06)
Marta.withdraw(10000)
Abebech.deposit(9000)
print(Marta.balance)
print(Abebech.balance)
Abebech.withdraw(10000)
print(Abebech.balance)