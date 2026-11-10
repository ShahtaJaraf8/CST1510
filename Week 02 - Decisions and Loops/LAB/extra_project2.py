print("Welcome to Jaraf's Treasure Island.")
print("Your mission is to find the treasure. You win or die, there is no third option")

# First choice (Left or Right)
choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n')

if choice1 == "left":
    # Second choice (Swim or Wait)
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    
    if choice2 == "wait":
        # Third choice (Doors)
        choice3 = input("You arrive at the island unharmed. There are 3 houses with 3 doors: one Red, one Yellow and one Blue. Which colour do you choose?\n")
        
        if choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "red":
            print("It's a room full of fire. You burnt to death.")
        elif choice3 == "blue":
            print("You enter a room of beasts. They ate you.")
        else:
            print("You chose a door that doesn't exist. You die.")
            
    else:
        print("You drown, because you can't swim.,")
        
else:
    print("You fell into a hole. Bye Bye.")