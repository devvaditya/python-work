#Pizza Order
print("Welcome to the Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

if size == "S":
    price = 15
    if add_pepperoni == "Y":
        price += 2
        if extra_cheese == "Y":
            price += 1
elif size == "M":
    price = 20
    if add_pepperoni == "Y":
        price += 3
        if extra_cheese == "Y":
            price += 1 
elif size == "L":
    price = 25
    if add_pepperoni == "Y":
        price += 3
        if extra_cheese == "Y":
            price += 1
else: 
    print("Sorry! This size is invalid.")
print("Your final bill is: $", price)