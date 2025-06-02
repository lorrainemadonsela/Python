class Transaction:
    def __init__(self, narration, amount, transaction_type):
        self.date_time = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.date_time} - {self.narration} - {self.transaction_type} - {self.amount}"

class Account:
    def __init__(self,loan_limit,account_number,account_owner_name,balances):
        self.balance = 0
        self.deposit = []
        self.withdrawal = []
        self.transactions = []
        self.loan_amount = 0
        self.minimum = 0
        self.loan_limit = loan_limit
        self.frozen = False
        self.account_number = account_number
        self.balances = balances
        self.account_owner_name = account_owner_name

    def deposit(self,amount,narration="Deposit"):
        if amount > 0:
            self.balance += amount
            self.deposit.append(amount)
            self.transactions.append(Transaction(narration, amount, "deposit"))
            print(f"Successful deposit, new balance is {self.balance}.")
        else:
            print("Invalid, enter a positive value.")

    def withdraw(self,amount, narration="Withdrawal"):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.withdrawal.append(amount)
            self.transactions.append(Transaction(narration, amount, "withdrawal"))
            print(f"Successful withdrawal, new balance is {self.balance}.")
        else:
            print(f"Insufficient funds.")

    def transfer_funds(self, amount, recipient_account):
        if amount > 0 and self.balances >= amount:
            self.balances -= amount
            recipient_account.balances += amount
            
            print(f"Successful transfer. Transferred {amount} from account {self.account_number} to account {recipient_account.account_number}.")
        else:
            print("Insufficient funds.")

    def calculate_balance(self):
        total_deposit = sum(self.deposit)
        total_withdrawal = sum(self.withdrawal)
        balance = total_deposit - total_withdrawal
        print(f"{balance}") 

    def check_loan_limit(self):
        available_limit = self.loan_limit - self.balance
        print(f"Your loan limit is {self.loan_limit}")
        print(f"Available loan limit is {available_limit}")

    def request_loan(self, amount):
        if amount <= 0:
            return "Invalid, enter a positive value."
        self.loan_amount += amount
        self.balance += amount
        self.transactions.append(f"{amount}")
        print(f"Loan of {amount} requested, new balance is {self.balance}")

    def repay_loan(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"{amount}")
            print(f"Loan of {amount} successful, new balance {self.balance}")

    def view_account_details(self):
        print(f"Account Number is {self.account_number}")
        print(f"Account Owner Name is {self.account_owner_name}")
        print(f"Current Balance is {self.balance}")

    def change_account_owner(self, new_name):
        self.account_owner_name = new_name
        print(f"Account owner name changed to {new_name}")

    def generate_statement(self):
        print("Transaction Statement")
        print(f"Account Number is {self.account_number}")
        print(f"Account Owner Name is {self.account_owner_name}")
        print("Transactions")
        for i, transaction in enumerate(self.transactions, start=1):
            print(f"{i}. {transaction}")
        print(f"Current Balance: {self.balance}")

    def calculate_interest(self,interest_rate):
        interest_amount = self.balance * (interest_rate / 100)
        self.balance += interest_amount
        self.transactions.append(f"{amount}")
        print(f"Interest of {interest_rate}% applied {interest_amount}")
        print(f"New balance is {self.balance}")

    def freeze_account(self):
        if not self.frozen:
            self.frozen = True
            print(f"Account {self.account_number} has been frozen.")
        else:
            print(f"Account {self.account_number} is already frozen.")

    def unfreeze_account(self):
        if self.frozen:
            self.frozen = False
            print(f"Account {self.account_number} has been unfrozen.")
        else:
            print(f"Account {self.account_number} is not frozen.")

    def set_minimum_balance(self, amount):
        self.minimum_balance = amount
        print(f"Minimum balance set to {self.minimum_balance}.")

    def close_account(self):
        self.balance = 0
        self.loan_amount = 0
        self.transactions = []
        print("Account closed.")