print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15  #small pizza: $15
elif size == "M":
    bill += 20  # Medium pizza: $20
elif size == "L":
    bill += 25  # Large pizza: $25

# Pepperoni pricing
if add_pepperoni == "Y":
    if size == "S":
        bill += 2  # Pepperoni on a small: +$2
    else:
        bill += 3  # Pepperoni on medium/large: +$3

# Extra cheese pricing
if extra_cheese == "Y":
    bill += 1  # Extra cheese, any size: +$1

# 3. Print "Your final bill is: $<amount>." exactly as specified
print(f"Your final bill is: ${bill}.")