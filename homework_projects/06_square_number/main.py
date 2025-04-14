def square_number():
    try:
        num = float(input("Type a number to see its square: "))
        
        print("The square of " + str(num) + " is " + str(num ** 2))
    
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == '__main__':
    square_number()