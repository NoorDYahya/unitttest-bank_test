########################
# Bank
########################
# This bank simulation build with arrays.
# In array - we present the money for each account
# Your bank account - index 0.
# We have more accounts in indexes 1,2,3
# The array looks like this:
#       [YourMoney , Account1Money , Account2Money , Account3Money]
# You have 100$. another accounts with 0$.

bank_accounts_money = [100, 0, 0, 0]

# check&return if x is greater than 0
def check_not_negative_or_zero(x):
    return x > 0

# safe cast to int
# if x is int -> return x
# else, return None
def convert_to_number(x):
    try:
        return int(x)
    except (ValueError, TypeError):
        return None

# The fee is 1$
FEE = 1
# Deposit money to your account
def deposit(amount):
    amount = convert_to_number(amount)
    if amount is not None:
        if(check_not_negative_or_zero(amount)):
            bank_accounts_money[0] += (amount-FEE)

# Withdraw money from your account
def withdraw(amount):
    amount = convert_to_number(amount)
    if amount is not None:
        if check_not_negative_or_zero(amount):
            if withdraw_check_balance(amount):
                bank_accounts_money[0] -= (amount+FEE)

# transfer money from your account to some account
# arguments:    to - number of account(index)
#               amount - how much money to transfer
def transfer(to, amount):
    to = convert_to_number(to)
    amount = convert_to_number(amount)
    if(amount is not None):
        if(check_not_negative_or_zero(amount) and withdraw_check_balance(amount)):
            if(to < len(bank_accounts_money)):
                bank_accounts_money[0] -= (amount + FEE)
                bank_accounts_money[to] += amount

# return True if there is enough money in your account - calculated with a fee
def withdraw_check_balance(amount):
    return bank_accounts_money[0] >= amount+FEE


# print all accounts
def printAllAccounts():
    print("======")
    for index in range(len(bank_accounts_money)):
        print("Account {}:{}".format(index, bank_accounts_money[index]))
    print("======")


# We have 5 options
# 1 - deposit
# 2 - withdraw
# 3 - transfer to account
# 4 - View all accounts
# 5 - exit
def main():
    while (True):
        print("plase select option:\n1 -Insert Cash\n2 -withdraw Cash\n3 -transfer\n4 -View All Accounts\n5 - Exit")
        selected = input("Select: ")  # the input is String
        selected = convert_to_number(selected)
        if selected == 1:
            x = input("How much: ")
            deposit(x)
        if selected == 2:
            x = input("How much: ")
            withdraw(x)
        if selected == 3:
            to = input("transfer to: ")
            amount = input("How much: ")
            transfer(to, amount)
        if selected == 4:
            printAllAccounts()
        if selected == 5:
            break

if __name__ == '__main__':
    main()
