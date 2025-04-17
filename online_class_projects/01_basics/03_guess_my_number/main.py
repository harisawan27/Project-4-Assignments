import random

def guess_my_number():
    secret_number: int = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")

    while True:
        user_input = input("Enter a guess: ")
        if not user_input.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        guess = int(user_input)

        while guess != secret_number:
            if guess < secret_number:
                print("Your guess is too low")
            else:
                print("Your guess is too high")

            print()  # Empty line for spacing

            user_input = input("Enter a new guess: ")
            if not user_input.isdigit():
                print("Invalid input. Please enter a valid number.")
                continue

            guess = int(user_input)

        print("Congrats! The number was:", secret_number)
        break

if __name__ == '__main__':
    guess_my_number()
