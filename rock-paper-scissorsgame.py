import random

# Function to get a random choice for the computer
def get_computer_choice():
    # Choices available in the game
    choices = ['rock', 'paper', 'scissors']
    # Randomly select a choice from the list
    return random.choice(choices)

# Function to determine the winner based on user and computer choices
def determine_winner(user_choice, computer_choice):
    # Check for a tie
    if user_choice == computer_choice:
        return "It's a tie!"
    # Check if the user wins based on game rules
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    # If it's not a tie or user win, then the computer wins
    else:
        return "Computer wins!"

# Main function to run the Rock-Paper-Scissors game
def rock_paper_scissors():
    # Initialize score counters for the user and computer
    user_score = 0
    computer_score = 0

    # Game introduction and instructions
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.")

    # Main game loop
    while True:
        # Get user input and ensure it’s valid
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue  # If invalid input, start the loop again

        # Get computer's choice by calling the function
        computer_choice = get_computer_choice()

        # Display both user and computer choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine and display the result
        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")

        # Update the scores based on the result
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        # Display current scores for both user and computer
        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Ask the user if they want to play another round
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':  # Exit the loop if the answer is not "yes"
            print("Thank you for playing Rock-Paper-Scissors!")
            break  # Exit the game loop

# Run the game by calling the main function
rock_paper_scissors()
