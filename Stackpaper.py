# Michael Suter
# using stack, apply it to scenario
# 3-10-20

from StackQ import Stack


def menu():
    choice = int(input("Enter a number between 1-5... >>"))
    while choice != 5:
        inventory = Stack
        while choice < 1 or choice > 5:
            if choice == 1:
                print("Disclaimer: The price of producing and shipping a case of paper is $20")
                add_to_inventory = int(input("How many cases of paper would you like to add to inventory? >>"))
                inventory = Stack.the_stack
                inventory = inventory + add_to_inventory
                price = 20
                cost = price * inventory
                print(f"The cost of this order is {cost}")
                Stack.push(inventory, add_to_inventory)
                print(f"there are now {inventory} cases of paper in the inventory.")
            elif choice == 2:
                print("Disclaimer: We sell the cases for $2 more by default")
                sell_amount = int(input(f"How many cases of paper do you want to sell out of the {inventory} in the inventory? >>"))
                sell_price = 22
                total_sale = sell_amount * sell_price
                print(f"You just sold {sell_amount} cases for {total_sale}")
                revenue = total_sale - cost
                print(f"")
                inventory = inventory - sell_amount
                Stack.pop(inventory)
                return
            elif choice == 3:
                print(f"the total revenue is {revenue}")
                return
            else:
                if choice == 4:
                    print(f"There are {inventory} cases available in the inventory")
                    return


print("""Enter 1 to add, 
    Enter 2 to sell,
    Enter 3 to see profit, 
    Enter 4 see the amount of cases in inventory, 
    Enter 5 to Quit""")

menu()
