def double_it():
    while True:
        user_input = input("Enter a number: ")
        try:
            curr_value = float(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    curr_value *= 2 

    while curr_value < 100:
        print(int(curr_value) if curr_value.is_integer() else curr_value)
        curr_value *= 2

    print(int(curr_value) if curr_value.is_integer() else curr_value)


if __name__ == '__main__':
    double_it()
