menu = {
    "pasta" : 40,
    "burger": 50,
    "biryani": 50,
    "cold drink": 70,
    "chicken": 130
}
print("Our menu is:\n Pasta : Rs 40\n Burger: Rs 50\n Biryani: Rs 50 \n Cold Drink: Rs 70 \n Chicken: 130")
total_order = 0
next_order = True
while next_order:
    item1 = input("Enter the item you want to order").lower()
    if item1 in menu:
        total_order += menu[item1]
        print(f"item {item1} added in your order")
        another_order = input("do you want to add another item in your order ? (Yes/N))").lower()
        if another_order == 'yes':
            next_order = True
        else:
            next_order = False
    else:
        print("{item1} is not available")
        another_order = input("do you want to add another item in your order ? (Yes/N))").lower()
        if another_order == 'yes':
            next_order = True

print(f"Your total bill is: {total_order}")


