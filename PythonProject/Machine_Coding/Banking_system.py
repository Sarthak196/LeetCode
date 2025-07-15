class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number in self.accounts:
            return f"Account {account_number} already exists."
        if initial_balance < 0:
            return "Initial balance cannot be negative."
        self.accounts[account_number] = initial_balance
        return f"Account {account_number} created with balance {initial_balance}."

    def close_account(self, account_number):
        if account_number not in self.accounts:
            return f"Account {account_number} does not exist."
        del self.accounts[account_number]
        return f"Account {account_number} has been closed."

class User(Bank):
    def __init__(self, account_number, initial_balance, accounts):
        self.account_number = account_number
        self.initial_balance = initial_balance
        self.accounts = accounts

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= 0:
                return "Deposit amount must be positive."
            self.accounts[account_number] += amount
            return f"Deposited {amount} to account {account_number}. New balance: {self.accounts[account_number]}."
        return f"Account {account_number} does not exist."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= 0:
                return "Withdrawal amount must be positive."
            if self.accounts[account_number] < amount:
                return "Insufficient funds."
            self.accounts[account_number] -= amount
            return f"Withdrew {amount} from account {account_number}. New balance: {self.accounts[account_number]}."
        return f"Account {account_number} does not exist."

    def get_balance(self, account_number):
        if account_number in self.accounts:
            return f"Balance for account {account_number}: {self.accounts[account_number]}."
        return f"Account {account_number} does not exist."

    def transfer(self, from_account, to_account, amount):
        if from_account not in self.accounts:
            return f"From account {from_account} does not exist."
        if to_account not in self.accounts:
            return f"To account {to_account} does not exist."
        if amount <= 0:
            return "Transfer amount must be positive."
        if self.accounts[from_account] < amount:
            return "Insufficient funds for transfer."

        self.accounts[from_account] -= amount
        self.accounts[to_account] += amount
        return f"Transferred {amount} from account {from_account} to account {to_account}. New balances: {from_account}: {self.accounts[from_account]}, {to_account}: {self.accounts[to_account]}."

if __name__ == "__main__":
    bank = Bank()
    user1 = User("12345", 1000, bank.accounts)
    user2 = User("67890", 500, bank.accounts)
    print(bank.create_account(user1.account_number, user1.initial_balance))
    print(bank.create_account(user2.account_number, user2.initial_balance))
    print(user1.deposit(user1.account_number, 200))
    print(user1.withdraw(user1.account_number, 150))
    print(user1.get_balance(user1.account_number))
    print(user1.transfer(user1.account_number, user2.account_number, 100))
    print(user2.get_balance(user2.account_number))
    print(bank.close_account(user1.account_number))


