class Account:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.deposit = []
        self.withdrawal = []
        self.transactions = []
        self.loan_amount = 0
        self.minimum = 0
        self.frozen = False

    def deposit(self,amount):
        self.deposit.append(amount)
        balance = self.get_balance()
        return f"Hello {self.name}, you have received {amount}. Your new balnce is {self.balance}"

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            return f"Insufficient funds. Minimum balance of ${self.minimum_balance} must be maintained."
        self.transactions.append(f"Withdrawal: -${amount}")
        return f"Withdrawal successful. New balance: ${self.balance}"

    def transfer_funds(self, amount, recipient_account):
        self.transactions.append(f"Transfer to {recipient_account.name}: -${amount}")
        recipient_account.transactions.append(f"Transfer from {self.name}: +${amount}")
        return f"Transfer successful. New balance: ${self.balance}"

    def get_balance(self):
        return f"Current balance: ${self.balance}"

    def request_loan(self, amount):
        self.transactions.append(f"Loan: +${amount}")
        return f"Loan of ${amount} approved. New balance: ${self.balance}"

    def repay_loan(self, amount):
        self.transactions.append(f"Loan repayment: -${amount}")
        return f"Loan repayment successful. Remaining loan balance: ${self.loan_amount}"

    def view_account_details(self):
        return f"Account Owner: {self.name}\nCurrent Balance: ${self.balance}"

    def change_account_owner(self, new_name):
        self.name = new_name
        return f"Account owner updated to {self.name}."

    def calculate_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        self.transactions.append(f"Interest: +${interest}")
        return f"Interest of ${interest} applied. New balance: ${self.balance}"

    def freeze_account(self):
        self.frozen = True
        return "Account frozen."

    def unfreeze_account(self):
        self.frozen = False
        return "Account unfrozen."

    def set_minimum_balance(self, amount):
        self.minimum_balance = amount
        return f"Minimum balance set to ${self.minimum_balance}."

    def close_account(self):
        self.balance = 0
        self.loan_amount = 0
        self.transactions = []
        return "Account closed."

account1 = Account("Mary Jane", 1000)
account2 = Account("Alfie Miller", 500)
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.transfer_funds(300, account2))
print(account1.get_balance())
print(account1.request_loan(1000))
print(account1.repay_loan(500))