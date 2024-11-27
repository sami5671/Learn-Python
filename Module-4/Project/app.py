from banking import Banking
from deposit import deposit
from withdraw import withdraw
from inquiry_balance import get_balance

ostad = Banking("Ostad", 50000)

while True:
    print("\n=================== Welcome to Ostader Banking System ==================\n")
    print("0. Exit")
    print("1. Deposits Money")
    print("2. Withdraw Money")
    print("3. Inquiry Balance")
    
    menu = input("\nSelect a number What do you want to do: ")

    if menu == "0": 
        print("\n============ Thanks for Using Ostader Bank ==========\n")
        break
    elif menu == "1":
        money = int(input("Enter the amount: "))
        print("\n============ Please Deposits Money =========\n")
        print(deposit(ostad, money))
      
    elif menu == "2":
        money = int(input("Enter the amount: "))
        print("\n============ Withdraw Money =========\n")
        print(withdraw(ostad, money))
       
    elif menu == "3":
        print("\n============ Inquiry Balance =========\n")
        print(get_balance(ostad))
    else: 
        print("Invalid option. Please try again.")
