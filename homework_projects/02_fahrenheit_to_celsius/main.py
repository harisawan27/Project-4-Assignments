def fahrenheit_to_celsius():
    user_input = input("Enter temperature in Fahrenheit (°F): ").strip()

    try:
        degrees_fahrenheit = float(user_input)

        degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

        print(f"Temperature: {degrees_fahrenheit}°F = {degrees_celsius}°C.")

    except ValueError:
        print("Error: Please enter a valid number for the temperature.")

if __name__ == '__main__':
    fahrenheit_to_celsius()