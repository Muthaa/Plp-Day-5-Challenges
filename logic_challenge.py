import os
import time

orders = {}

def coffee_or_tea():
    """Main function to handle drink ordering logic."""
    os.system("cls")

    while True:
        print("   |||Coffee/Tea Machine Decision Maker|||   ")
        print("  ----------------------------------- ")
        print()

        try:
            # Ask user for their choice of drink
            user_input = input("Would you like a. Coffee or b. Tea (or 'none' to exit): ").lower()

            if user_input == "none":  # Exit condition
                break
            elif user_input == "a":  # Coffee option
                user_drink = input("a. Black or b. Milk: ").lower()

                if user_drink == "a":  # Black coffee
                    user_name = input("Name?: ").capitalize()
                    orders[user_name] = "Black Coffee"
                    print(f"Black Coffee for {user_name} coming right up. Proceed to pay point.")
                elif user_drink == "b":  # Coffee with milk
                    user_name = input("Name?: ").capitalize()
                    orders[user_name] = "Coffee with Milk"
                    print(f"Coffee with Milk for {user_name} coming right up. Proceed to pay point.")
                else:
                    print("Pick a valid option for coffee.")

            elif user_input == "b":  # Tea option
                user_drink = input("a. Green Tea or b. Tea with Milk: ").lower()

                if user_drink == "a":  # Green Tea
                    user_name = input("Name?: ").capitalize()
                    orders[user_name] = "Green Tea"
                    print(f"Green Tea for {user_name} coming right up. Proceed to pay point.")
                elif user_drink == "b":  # Tea with milk
                    user_name = input("Name?: ").capitalize()
                    orders[user_name] = "Tea with Milk"
                    print(f"Tea with Milk for {user_name} coming right up. Proceed to pay point.")
                else:
                    print("Pick a valid option for tea.")

            else:
                print("Pick a valid option for coffee or tea.")

        except EOFError:
            print("No input received. Exiting program.")
            break

    print("\nOrders Summary:")
    for name, drink in orders.items():
        print(f"{name} ordered: {drink}")
