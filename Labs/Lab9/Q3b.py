class BankAcc:
    def __init__(self, name="", address="", funds=0, iban="", acc_num=0):
        self.name1 = name
        self.address1 = address
        self.funds1 = funds
        self.IBAN1 = iban
        self.acc_num1 = acc_num
        self.transactions = []

    def enter_transactions(self):
        transactions2 = []
        for i in range(0, 5):
            print("Enter paid amount of transaction number ", i,)
            temp = float(input())
            transactions2.append(temp)
        return transactions2

    def withdraw(self, withdraw_amount):
        self.funds1 = self.funds1 - withdraw_amount
        # Record
        transaction3 = self.transactions
        withdraw_amount = withdraw_amount * -1
        transaction3.append(withdraw_amount)

    def deposit(self, deposit_amount):
        self.funds1 = self.funds1 + deposit_amount
        # Record
        transaction3 = self.transactions
        transaction3.append(deposit_amount)
        self.transactions = transaction3

    def __str__(self):
        return_str = "Name: {}\nAddress: {}\nBalance: {}\nIBAN: {}\nAccount Number: {}\nTransacations: {}\n".format(
            self.name1, self.address1, self.funds1, self.IBAN1, self.acc_num1, self.transactions)
        return return_str
        
# main
account1 = BankAcc('Jack Levins', 'Dublin St.', 1200, 'IE04123456789BOFI987654321', 1234567)
print(account1)
account1.deposit(1200)
print(account1)        