import random
import time
import sys


def get_choices():
    abbreviations = {"r": "rock", "p": "paper", "s": "scissors"}
    player_input = input("Enter a choice (rock, paper, scissors): ").lower()
    # Check if the input is an abbreviation, if not, use the input as is
    player_choice = abbreviations.get(player_input, player_input)
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player}, the computer chose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors!! YOU WIN!!"
        else:
            return "Paper covers rock. YOU LOSE"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper!! YOU WIN!!"
        else:
            return "Rock smashes scissors. YOU LOSE"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock!! YOU WIN!!"
        else:
            return "Scissors cuts paper. YOU LOSE"


# Initialize scores
player_score = 0
computer_score = 0

while True:
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)

    # Update scores
    if "YOU WIN" in result:
        player_score += 1
    elif "YOU LOSE" in result:
        computer_score += 1

    # Display scores
    print(f"Player Score: {player_score}, Computer Score: {computer_score}")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes" and play_again != "y":
        print("Thanks for playing! Final scores:")
        print(f"Player Score: {player_score}, Computer Score: {computer_score}")
        # animation at end
        animation = "THANKS FOR PLAYING!!!!!!!!!!!"
        colors = ['\033[91m', '\033[93m', '\033[92m', '\033[94m', '\033[95m', '\033[96m']
        reset_color = '\033[0m'

        start_time = time.time()

        while True:
            for i in range(len(animation)):
                time.sleep(0.1)  # Speed
                colored_char = colors[i % len(colors)] + animation[i] + reset_color
                sys.stdout.write(colored_char)
                sys.stdout.flush()

            if time.time() - start_time > 2.7:  # length in seconds
                break

        sys.stdout.write("\rBYE")
        break
