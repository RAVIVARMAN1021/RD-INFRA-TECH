import random

def get_user_choice():
    while True:
        user_input = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid input. Please choose Rock, Paper, or Scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, result):
    print(f"\nYou chose: {user.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")
    if result == "tie":
        print("Result: It's a tie!")
    elif result == "user":
        print("Result: You win! ")
    else:
        print("Result: You lose! ")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock-Paper-Scissors Game ---")
        user = get_user_choice()
        computer = get_computer_choice()
        result = determine_winner(user, computer)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        display_result(user, computer, result)
        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

play_game()
