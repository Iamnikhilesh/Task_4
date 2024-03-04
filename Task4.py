# Rock-Paper-Scissors Game
import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        print("Score - You: {}, Computer: {}".format(user_score, computer_score))

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("\nYour choice: {}".format(user_choice))
        print("Computer's choice: {}".format(computer_choice))

        result = determine_winner(user_choice, computer_choice)
        print("\nResult: {}".format(result))

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    rock_paper_scissors_game()
