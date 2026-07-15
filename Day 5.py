class Account:
    def __init__ (self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance    

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if self._balance < amount:
            raise ValueError("Insufficient Fund")    
        self._balance -= amount
   
    def statement(self):
        print(f"Account Type: Regular Account")
        print(f"Owner: {self.owner}")
        print(f"Account number: {self.account_number}")
        print(f"Balance: {self._balance}")


class SavingsAccount (Account):
    def __init__(self, owner, account_number, balance, rate=0.07):
        super().__init__(owner, account_number, balance)
        self.rate =rate
   
    def add_interest(self):
        self._balance += self._balance * self.rate

    def statement(self):
        print(f"Account Type: Saving Account")
        print(f"Owner: {self.owner}")
        print(f"Account number: {self.account_number}")
        print(f"Interest rate: {self.rate*100}%")
        print(f"Balance: {self._balance}")


class CurrentAccount(Account):
    def __init__(self, owner, account_number, balance, overdraft_limit=5000):
        super().__init__(owner, account_number, balance)
        self.overdraft = overdraft_limit
    
    def withdraw(self,amount):
        if amount > self._balance + self.overdraft:
            raise ValueError("Insufficient Fund")   
        self._balance -= amount

    def statement(self):
        print(f"Account Type: Current Account")
        print(f"Owner: {self.owner}")
        print(f"Account number: {self.account_number}")
        print(f"Overdraft limit: {self.overdraft}")
        print(f"Balance: {self._balance}")
        


Accounts = [Account("Abebech", 100001, 0), CurrentAccount("Marta", 100002, 0)]

Abebech = Accounts[0]
Marta = Accounts[1]


Marta.deposit(36767.06)
Marta.withdraw(40000)
Abebech.deposit(9000)
Abebech.withdraw(1000)

for account in Accounts:
    account.statement()
    