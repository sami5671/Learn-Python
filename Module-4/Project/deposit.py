def deposit(account, amount):
    if amount > 0:
        account.initial_balance += amount
        return f"You have deposited {amount}. current balance: {account.initial_balance}"
    else: 
        return "Invalid deposit amount. Please enter a positive value."
        