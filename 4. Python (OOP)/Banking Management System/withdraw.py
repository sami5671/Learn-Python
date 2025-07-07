def withdraw(account, amount):
    if account.initial_balance > amount and (account.initial_balance - amount) > 500:
        account.initial_balance -= amount
        return f"Withdrew {amount} from account {account.user_name}. Remaining balance: {account.initial_balance}"
    else:
        return "Insufficient funds in the account"