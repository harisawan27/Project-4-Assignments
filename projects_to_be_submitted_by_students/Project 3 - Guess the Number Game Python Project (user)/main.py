import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    print("\n🕹️  WELCOME TO THE GUESS THE NUMBER GAME!")
    print("I've picked a number between 1 and 100. Can you figure it out?")

    attempts = 0

    while True:
        guess = input("\n🔢 Enter your guess: ")

        if not guess.isdigit():
            print("⚠️  Oops! Please type a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("📉 Too low! Try a bigger number.")
        elif guess > number_to_guess:
            print("📈 Too high! Try a smaller number.")
        else:
            print(f"\n🎉 You got it! The number was {number_to_guess}.")
            print(f"👏 It took you {attempts} tries. Well done!")
            break

if __name__ == "__main__":
    guess_the_number()
