num1 = 4
num2 = 5

answer = int(input(f"What is {num1}+{num2}?"))

if answer == num1 + num2:
    print("Correct")
else:
    print(f"Incorrect. The correct answer is {num1 + num2}")


#%%


import random
while True:
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)

    answer = int(input(f"What is {num1}+{num2}?"))
    if answer == num1 + num2:
        print("Correct")
        break
    else:
        print("Try again")

# %%
