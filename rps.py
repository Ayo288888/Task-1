import random

def get_user_choice():
    """Get and validate the user's choice"""
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        user_input = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower().strip()
        
        if user_input == 'quit':
            return None
        elif user_input in choices:
            return user_input
        else:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    """Generate a random choice for the computer"""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on Rock, Paper, Scissors rules"""
    if user_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        'rock': 'scissors',      
        'paper': 'rock',        
        'scissors': 'paper'      
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    """Display the choices and result"""
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    """Main game function"""
 

    user_score = 0
    computer_score = 0
    ties = 0
    
    while True:
     
        user_choice = get_user_choice()
        
      
        if user_choice is None:
            break
        
        computer_choice = get_computer_choice()
        
        
        winner = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, winner)
   
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        else:
            ties += 1
        
    
        print(f"\nCurrent Score - You: {user_score}, Computer: {computer_score}, Ties: {ties}")
        print("-" * 60)
    

    print("\nFinal Score:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties: {ties}")
    
    if user_score > computer_score:
        print("Congratulations! You won overall!")
    elif computer_score > user_score:
        print("Computer won overall! Better luck next time!")
    else:
        print("It's a tie overall! Great game!")
    
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()