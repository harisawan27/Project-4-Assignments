import random
import string

def choose_word():
    word_list = ["coding", "football", "python", "cricket", "hangman", "study", "tea", "laptop"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman_game():
    print("\n🎉 WELCOME TO THE HANGMAN CHALLENGE!")
    print("Try to guess the word one letter at a time.\n")

    word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print(f"\n🕒 Attempts left: {attempts}")
        print(f"🔤 Word: {display_word(word, guessed_letters)}")

        guess = input("👉 Enter a letter: ").lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("⚠️  Please enter a single valid letter (a-z).")
            continue

        if guess in guessed_letters:
            print("🔁 You already tried that one. Try a new letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ Nice! The letter '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"❌ Nope! The letter '{guess}' isn’t in the word.")

        if all(letter in guessed_letters for letter in word):
            print(f"\n🎊 Congrats! You figured it out. The word was: '{word}'")
            break
    else:
        print(f"\n💀 Game Over! You ran out of tries. The word was: '{word}'")

if __name__ == "__main__":
    hangman_game()
