def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Convert Celsius to Fahrenheit
celsius_value = float(input("Enter temperature in Celsius: "))
fahrenheit_result = celsius_to_fahrenheit(celsius_value)
print(f"{celsius_value} Celsius is equal to {fahrenheit_result} Fahrenheit")

# Convert Fahrenheit to Celsius
fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
celsius_result = fahrenheit_to_celsius(fahrenheit_value)
print(f"{fahrenheit_value} Fahrenheit is equal to {celsius_result} Celsius")
