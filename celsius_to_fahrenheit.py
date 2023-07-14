
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

# Convert Celsius to Fahrenheit
if unit.upper() == "C":
    fahrenheit = celsius_to_fahrenheit(temperature)
    print(f"{temperature} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
    
# Convert Fahrenheit to Celsius
elif unit.upper() == "F":
    celsius = fahrenheit_to_celsius(temperature)
    print(f"{temperature} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
    
# Invalid unit
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
