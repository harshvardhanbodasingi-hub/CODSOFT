# Task 4: Rock-Paper-Scissors Game - CodSoft

import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def decide_winner(user, comp):
    if user == comp:
        return "draw"
    if (user == "rock" and comp == "scissors") or \
       (user == "paper" and comp == "rock") or \
       (user == "scissors" and comp == "paper"):
        return "user"
    return "computer"


def main():
    print("=" * 45)
    print("        ROCK - PAPER - SCISSORS GAME")
    print("=" * 45)

    user_score = 0
    comp_score = 0

    while True:
        user = input("\nEnter rock, paper, scissors (or 'exit' to quit): ").lower().strip()

        if user == "exit":
            break

        if user not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please type rock, paper, or scissors.")
            continue

        comp = get_computer_choice()
        print(f"Computer chose: {comp}")

        result = decide_winner(user, comp)

        if result == "draw":
            print("It's a draw!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            comp_score += 1

        print(f"Score -> You: {user_score} | Computer: {comp_score}")

    print("\nFinal Score:")
    print(f"You: {user_score} | Computer: {comp_score}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
