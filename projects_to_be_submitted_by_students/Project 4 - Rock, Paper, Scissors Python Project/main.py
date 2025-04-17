import random

def play_game():
    choices = ["rock", "paper", "scissors"]

    print("\n🪨📄✂️  LET'S PLAY ROCK, PAPER, SCISSORS!")
    print("Can you outsmart the computer?")

    user_choice = input("\n👉 Choose one (rock / paper / scissors): ").lower()

    if user_choice not in choices:
        print("⚠️  That’s not a valid move. Try typing rock, paper, or scissors.")
        return

    computer_choice = random.choice(choices)
    print(f"\n🤖 The computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a tie! Great minds think alike.")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win! That was a solid move.")
    else:
        print("💻 The computer wins this time! Better luck next round.")

if __name__ == "__main__":
    play_game()
