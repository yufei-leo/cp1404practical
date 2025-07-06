# temperatures.py

# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"Fahrenheit: {celsius_to_fahrenheit(celsius)}")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"Celsius: {fahrenheit_to_celsius(fahrenheit)}")
