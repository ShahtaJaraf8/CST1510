import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# --- Step 2, 3 & 4: The Hand Class ---
class Hand:
    def __init__(self):
        # Step 2: Initialize with an empty list of cards
        self.cards = []
        
    def add_card(self):
        # Step 3: Deal a card and append it to self.cards
        card = deal_card()
        self.cards.append(card)
        
    def score(self):
        # Step 4: Calculate score based on Blackjack rules
        # Check for a blackjack (2 cards totaling 21)
        if sum(self.cards) == 21 and len(self.cards) == 2:
            return 0  # 0 represents a Blackjack
        
        # Handle Ace (11 or 1) if the score goes over 21
        current_score = sum(self.cards)
        if 11 in self.cards and current_score > 21:
            self.cards.remove(11)
            self.cards.append(1)
            current_score = sum(self.cards)
            
        return current_score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Lose, opponent has Blackjack "
    elif user_score == 0:
        return "Win with a Blackjack "
    elif user_score > 21:
        return "You went over. You lose "
    elif computer_score > 21:
        return "Opponent went over. You win "
    elif user_score > computer_score:
        return "You win "
    else:
        return "You lose "

def play_game():
    print("Welcome to Object-Oriented Blackjack!")
    
    # --- Step 6: Represent players using Hand objects ---
    user_hand = Hand()
    computer_hand = Hand()
    
    is_game_over = False
    
    # Deal initial 2 cards to each hand
    for _ in range(2):
        user_hand.add_card()
        computer_hand.add_card()
        
    while not is_game_over:
        # --- Step 7: Use method calls instead of separate functions ---
        user_score = user_hand.score()
        computer_score = computer_hand.score()
        
        print(f"   Your cards: {user_hand.cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_hand.cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_hand.add_card()
            else:
                is_game_over = True
                
    # Computer plays until score is 17 or more
    while computer_score != 0 and computer_score < 17:
        computer_hand.add_card()
        computer_score = computer_hand.score()
        
    print(f"   Your final hand: {user_hand.cards}, final score: {user_hand.score()}")
    print(f"   Computer's final hand: {computer_hand.cards}, final score: {computer_score}")
    
    # --- Step 8: Update comparison with object scores ---
    print(compare(user_hand.score(), computer_score))

# Run the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()