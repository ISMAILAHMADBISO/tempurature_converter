def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * 5/9

# Prompt the user for input
print("Temperature Conversion Program")
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit): ").strip().upper()

# Perform the conversion
if unit == 'C':
    converted = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is equal to {converted:.2f}°F.")
elif unit == 'F':
    converted = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is equal to {converted:.2f}°C.")
else:
    print("Invalid unit entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
