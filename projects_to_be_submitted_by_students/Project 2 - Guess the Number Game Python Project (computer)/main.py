import random

def number_guess_computer():
    print("🎯 Think of a number between 1 and 100, and I'll try to guess it.")
    input("👉 Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        guess = random.randint(low, high)
        attempts += 1

        print(f"\n🤖 My guess is: {guess}")
        feedback = input("Is my guess too high, too low, or correct? (Type: high / low / correct): ").lower()

        if feedback == "correct":
            print(f"\n🎉 I guessed your number {guess} in {attempts} attempts!")
            break
        elif feedback == "high":
            high = guess - 1
        elif feedback == "low":
            low = guess + 1
        else:
            print("❌ Oops! Please type 'high', 'low', or 'correct'.")

if __name__ == "__main__":
    number_guess_computer()
