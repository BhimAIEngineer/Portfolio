import random

def play_rps():
    # Game options
    choices = ["rock", "paper", "scissors"]
    
    # Starting scores
    user_score = 0
    computer_score = 0
    
    # Welcome message
    print("\n" + "="*50)
    print("Bhim's ROCK PAPER SCISSORS GAME")
    print("="*50)
    
    # Main game loop
    while True:
        # Show current score
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")
        
        # Show menu
        print("\n1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        
        try:
            # Get user input
            user_choice = int(input("\nChoose (1-4): "))
            
            # Quit game
            if user_choice == 4:
                print(f"\nFinal Score - You: {user_score} | Computer: {computer_score}")
                
                if user_score > computer_score:
                    print("You won the game! Congratulations!")
                elif user_score < computer_score:
                    print("Computer won the game! Better luck next time!")
                else:
                    print("It's a tie!")
                
                print("Thanks for playing!")
                break
            
            # Check for valid choice
            if user_choice not in [1, 2, 3]:
                print("Invalid choice! Choose 1-4")
                continue
            
            # Convert number to choice name
            user_choice_name = choices[user_choice - 1]
            
            # Computer randomly chooses
            computer_choice = random.choice(choices)
            
            # Show what each player chose
            print(f"\nYou chose: {user_choice_name}")
            print(f"Computer chose: {computer_choice}")
            
            # Determine the winner
            if user_choice_name == computer_choice:
                print("It's a tie!")
                
            elif (user_choice_name == "rock" and computer_choice == "scissors"):
                print("You win this round!")
                user_score += 1
                
            elif (user_choice_name == "paper" and computer_choice == "rock"):
                print("You win this round!")
                user_score += 1
                
            elif (user_choice_name == "scissors" and computer_choice == "paper"):
                print("You win this round!")
                user_score += 1
                
            else:
                print("Computer wins this round!")
                computer_score += 1
                
        except ValueError:
            print("Invalid input! Please enter a number.")

# Start the game
if __name__ == "__main__":
    play_rps()