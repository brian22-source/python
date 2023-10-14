balance = 18000


def check_balance():
    print("Your balance is: ${: .2f}".format(balance))


def deposit():
    global balance
    deposit_amount = float(input("Enter your deposit amount: "))
    if deposit_amount > 0:
        balance += deposit_amount
        print("${:.2f} has been deposited.".format(deposit_amount))
    else:
        print("Invalid deposit.")


def withdrawal():
    global balance
    withdrawal_amount = float(input("Enter amount to withdrawal: "))
    if withdrawal_amount > 0 and withdrawal_amount <= balance:
        balance -= withdrawal_amount
        print("${:.2f} has been withdrawn.".format(withdrawal_amount))
    elif withdrawal_amount > balance:
        print("Insufficient balance.")
    else:
        print("Invalid input/Invalid withdrawal amount.")


while True:
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")
    choice = input("Please select an option (1/2/3/4): ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdrawal()
    elif choice == "4":
        print("Thank you for visiting us.")
        break
    else:
        print("Invalid option.")
