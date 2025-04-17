import random
import string

def create_strong_password(length, allow_uppercase=True, allow_digits=True, allow_symbols=True):
    characters = string.ascii_lowercase

    if allow_uppercase:
        characters += string.ascii_uppercase
    if allow_digits:
        characters += string.digits
    if allow_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def run_password_maker():
    print("\n🔐 Welcome to the Simple Password Maker!")

    try:
        length = int(input("🔢 How many characters long should your password be? "))

        if length < 6:
            print("⚠️ Password should be at least 6 characters long.")
            return

        upper = input("🅰️ Include uppercase letters? (yes/no): ").strip().lower() == "yes"
        digits = input("🔢 Include numbers? (yes/no): ").strip().lower() == "yes"
        symbols = input("💥 Include special characters? (yes/no): ").strip().lower() == "yes"

        final_password = create_strong_password(length, upper, digits, symbols)

        print("\n🔏 Your secure password is:")
        print(final_password)

    except ValueError:
        print("❌ Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    run_password_maker()
