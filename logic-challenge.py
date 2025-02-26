import sys
import os
import time

orders = {}

os.system("cls")

while True:
    print("""   |||Coffee/Tea Machine Decision Maker|||   """)
    print("""  ----------------------------------- """)
    print()

    try:
        # Ask user for their choice of drink
        user_input = input("Would you like a. Coffee or b. Tea (or 'none' to exit): ")

        if user_input.lower() == "none":  # Exit condition
            break
        elif user_input == "a":  # Coffee option
            user_drink = input("a. Black or b. Milk: ")

            if user_drink == "a":  # Black coffee
                user_name = input("Name?: ").capitalize()
                orders[user_name] = "Black Coffee"  # Add to orders dictionary
                print(
                    "Black Coffee for "
                    + user_name
                    + " coming right up. Proceed to pay point."
                )
                time.sleep(5)
                os.system("cls")


            elif user_drink == "b":  # Coffee with milk
                user_name = input("Name?: ").capitalize()
                orders[user_name] = "Coffee with Milk"  # Add to orders dictionary
                print(
                    "Coffee with Milk for "
                    + user_name
                    + " coming right up. Proceed to pay point."
                )
                time.sleep(5)
                os.system("cls")

            else:
                print("Pick a valid option for coffee.")

        elif user_input == "b":  # Tea option
            user_drink = input("a. Green Tea or b. Tea with Milk: ")

            if user_drink == "a":  # Green Tea
                user_name = input("Name?: ").capitalize()
                orders[user_name] = "Green Tea"  # Add to orders dictionary
                print(
                    "Green Tea for "
                    + user_name
                    + " coming right up. Proceed to pay point."
                )
                time.sleep(5)
                os.system("cls")

            elif user_drink == "b":  # Tea with milk
                user_name = input("Name?: ").capitalize()
                orders[user_name] = "Tea with Milk"  # Add to orders dictionary
                print(
                    "Tea with Milk for "
                    + user_name
                    + " coming right up. Proceed to pay point."
                )

            else:
                print("Pick a valid option for tea.")

        else:
            print("Pick a valid option for coffee or tea.")

    except EOFError:
        print("No input received. Exiting program.")
        break

# Display orders after the program ends (if you want to see the list of orders)
print("\nOrders Summary:")
for name, drink in orders.items():
    print(f"{name} ordered: {drink}")
