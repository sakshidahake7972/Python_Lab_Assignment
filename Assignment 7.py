#1 - Menu Driven Calculator

# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     if b == 0:
#         return "Error! Division by zero."
#     return a / b
#
# def modulus(a, b):
#     if b == 0:
#         return "Error! Modulus by zero."
#     return a % b
#
#
# while True:
#     print("\n----- CALC MENU -----")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Modulus")
#     print("6. Exit")
#
#     choice = int(input("Enter your choice (1-6): "))
#
#     if choice == 6:
#         print("Exiting Calculator...")
#         break
#
#     if choice in [1, 2, 3, 4, 5]:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#
#         if choice == 1:
#             print("Result:", add(num1, num2))
#         elif choice == 2:
#             print("Result:", subtract(num1, num2))
#         elif choice == 3:
#             print("Result:", multiply(num1, num2))
#         elif choice == 4:
#             print("Result:", divide(num1, num2))
#         elif choice == 5:
#             print("Result:", modulus(num1, num2))
#     else:
#         print("Invalid Choice! Please try again.")



# Lab Assignment 2 - Bank Account Program

balance = 0.0

def display_balance():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited Successfully.")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        print("Amount Withdrawn Successfully.")


while True:
    print("\n----- BANK MENU -----")
    print("1. Display Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 4:
        print("Thank you for using the Bank System.")
        break

    if choice == 1:
        display_balance()

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            deposit(amount)
        else:
            print("Invalid Amount!")

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0:
            withdraw(amount)
        else:
            print("Invalid Amount!")

    else:
        print("Invalid Choice! Please try again.")