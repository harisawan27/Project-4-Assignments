def agreement_bot():
    favorite_animal = input("What's your favorite animal? ").strip()

    if favorite_animal == "" or not favorite_animal.isalpha():
        print("Error: Please enter a valid animal name using only letters.")
    else:
        print("My favorite animal is also " + favorite_animal + "!")

if __name__ == '__main__':
    agreement_bot()