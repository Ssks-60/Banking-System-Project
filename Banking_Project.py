import random 
from datetime import datetime
#create account

accounts = {}
# make the create account function
#1.
def create_account():
    name = input("Enter your name: ") 
    pin = input("Create a 4-digit PIN: ")  
    account_number = random.randint(100000, 999999)
    accounts[account_number] = {
        "name": name,
        "pin" : pin,
        "balance" : 0,
        "transactions" : []
    }

    print("\nAccount created successfully!")
    print("Your account number is:", account_number)
#2.
def login():
    account_number = int(input("Enter your account number: " ))
    pin = input("Enter your PIN:")

    if account_number in accounts and accounts[account_number]["pin"] == pin :  
        print("\nLogin successfully!")
        print("Welcome,", accounts[account_number]["name"])
        account_menu(account_number)
    else:
        print("\nInvalid account number or PIN.")

#3.
def account_menu(account_number):
    while True:
        print("\n======= ACCOUNT MENU =======")
        print("1. Check Balance ")
        print("2. Deposit ")
        print("3. Withdraw ")
        print("4. Transfer ")
        print("5. Transaction History ")
        print("6. Change PIN ")
        print("7. Logout ")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Your balance is:", accounts[account_number]["balance"])

        elif choice == "2":
            deposit(account_number)
        elif choice == "3" :
            withdraw(account_number)
        elif choice == "4":
            transfer_money(account_number)
        elif choice == "5":
            show_transaction(account_number)   
        elif choice == "6":
            change_pin(account_number)
    
        elif choice == "7" :
            print("Logged out successfully!") 
            return
        
        else:
            print("This feature is coming next. ")


#4.
def deposit(account_number):
    amount = float(input("Enter amount to deposit: "))
    if amount > 0 :
        accounts[account_number]["balance"] += amount
        accounts[account_number]["transactions"].append(f"Deposited ₹ {amount} on {datetime.now()}")

        print("Deposit successful!")
        print("New balance:", accounts[account_number]["balance"])
    else:
        print("Amount must be greater than 0.")
        

#5.
def withdraw(account_number):
    amount = float(input("Enter amount to withdraw: "))
    if amount > 0:
        if amount <= accounts[account_number]["balance"]:

            accounts[account_number]["balance"] -= amount

            accounts[account_number]["transactions"].append(f"Withdrawn ₹ {amount} ")
            print("Withdrawal successful!")
            print("New balance:", accounts[account_number]["balance"])
        else:
            print("Insufficient balance.")
    else:
        print("Amount must be greater than 0.")

#6.
def show_transaction(account_number):
    print("\n----- Transaction History -----")
    transactions = accounts[account_number]["transactions"]

    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(transaction)

#7.
def account_details(account_number):
    print("\n ---- Account Details ----")
    print("Account Number:", account_number)
    print("Name: ", accounts[account_number]["name"])
    print("Balance:", accounts[account_number]["balance"])


#8.FOR CHANGING THE PIN
def change_pin(account_number):
    old_pin = input("Enter current PIN: ")
    if old_pin == accounts[account_number]["pin"]:
        new_pin = input("Enter new PIN: ") 
        accounts[account_number]["pin"] = new_pin
        print("PIN changed successfully!")
    else:
        print("Incorrect current PIN.")    

#9.TRANSFER MONEY 
def transfer_money(account_number):
    
    receiver_account =int(input("Enter receiver account number: "))

   
    
    if receiver_account not in accounts:
        print("Receiver account not found.")
        return

    if account_number == receiver_account:
        print("you cannot transfer money to your own account.")
        return
    
    
    amount = float(input("Enter amount to transfer: "))
    if amount <= 0:
        print("Amount must be greater than 0.")
        return
    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
        return

    accounts[account_number]["balance"] -= amount 
    accounts[receiver_account]["balance"] += amount
    
    print("Transfer successful!")
    print("Receiver:", accounts[receiver_account]["name"])
    print("Amount transferred:", amount)
    print("Remaining balance", accounts[account_number]["balance"])


create_account()
create_account()
login()
