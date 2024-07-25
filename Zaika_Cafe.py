from art import logo
print(logo)
print("Welcome in Zaika")
menu = {
    "chowmin" : 70,
    "cold drink": 50,
    "chicken rice": 130,
    "biryani": 140,
    "roasted chicken": 250,
    "pasta": 70,
    "cold coffee": 60,
    "chhola rice": 60,
    "sandwitch":20
}
print("Our Menu:")
print("-----------------")
total_order = 0
for item, price in menu.items():
    print(f"{item} : Rs.{price}")

next_order = True
while next_order:
    order = input("Enter the name of item you want add in order").lower()
    if order in menu:
        total_order += menu[order]
        print(f"{order} added in your order")
        another_order = input("Do you want to add another item? pres(yes/no").lower()
        if another_order == 'yes':
            next_order = True
        else:
            next_order = False
    else:
        print(f"{order} is not available")
        another_order = input("Do you want to add another item? pres(yes or no)").lower()
        if another_order == 'yes':
            next_order = True
        else:
            next_order = False

print(f"Your total bill is : Rs.{total_order}")
