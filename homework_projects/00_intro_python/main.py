def add2numbers():
    print("This program adds two numbers.~")

    try:
        num1 = int(input("Enter first number: "))

        num2 = int(input("Enter second number: "))

        total = num1 + num2

        print("The total is " + str(total) + ".")

    except ValueError:
        print("Error: Please enter valid integers only.")

if __name__ == '__main__':
    add2numbers()