## ATM Simulator mini project using Python programming language

print("Welcome to SBI Bank")
Pin = 7878
chances = 3
balance = 50000
while chances != 0:
    user_pin = int(input("Please enter the four digit pin : "))
    if user_pin != Pin:
        chances -= 1
        print("Wrong pin Number")
        print(f"You have {chances} chances left")
    else:
        user_choice = input("B : balance, D : deposit, W : withdraw : ")
        if user_choice == "B":
            print(f"Your total balance is {balance}")

        if user_choice == "D":
            deposit_user = int(input("Enter the amount that you would like to deposit : "))
            total_balance = deposit_user + balance
            print(f"You have deposit RS.{deposit_user}")
            print(f"Your total balance is {total_balance}")

        if user_choice == "W":
            withdraw_user = int(input("Enter the amount you want to withdraw : "))
            total_balance = balance - withdraw_user
            print(f"You have withdraw Rs.{withdraw_user}")
            print(f"Your total balance is Rs.{total_balance}")

    user_exit = input("Would you like to exit? Yes/No : ")
    if user_exit == "Yes":
        print("Thankyou for using SBI Bank ")
        break
    else:
        continue

     
        
















































