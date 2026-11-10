import random

friends = ["Alice", "Bob", "Charlie", "Dana", "Ella"]

print("--- Version 1: Using random.choice() ---")

payer = random.choice(friends)

print(f"{payer} is paying the bill today!")

print("\n--- Version 2: Using random.randint() and an index ---")

num_friends = len(friends)

index = random.randint(0, num_friends - 1)

payer = friends[index]

print(f"{payer} is paying the bill today!")