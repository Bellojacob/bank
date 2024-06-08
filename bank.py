# Bank Function App


user_x_balance = 100;


def check_balance():
   global user_x_balance
   return f'Your balance is ${user_x_balance}   \n'


def deposit():
   global user_x_balance
   deposit_Amount = input("How much would you like to deposit? ")
   deposit_Amount = int(deposit_Amount)
   if deposit_Amount > 0:
       user_x_balance = user_x_balance + deposit_Amount
       print(f"Successfully Deposited {deposit_Amount}")
       return user_x_balance
   else:
       return f"Invalid amount: {deposit_Amount}, please try again."


def withdrawl():
   pass


def main():
   running = True


   while running:
       print("Welcome to ABC Bank, make a selection to continue.")
       print("1. Check Balance")
       print("2. Deposit")
       print("3. Withdrawl")
       print("4. Exit")
       choice = input("Enter a choice (1-4): ")
       print("\n")
       if choice == "1":
           print(check_balance())
       elif choice == "2":
           deposit()
       elif choice == "3":
           withdrawl()
       elif choice == "4":
           print("Thank you for banking with ABC!")
           running = False
       else:
           print("Invalid choice, please try again.")
           main()


main()

