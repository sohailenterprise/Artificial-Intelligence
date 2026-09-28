def convert_temperature(value, to_unit="Fahrenheit"):
    if to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif to_unit == "Kelvin":
        return value + 273.15


print("25C in Fahrenheit (default):", convert_temperature(25))

print("25C in Kelvin:", convert_temperature(25, "Kelvin"))

print("100C in Kelvin:", convert_temperature(value=100,to_unit="Kelvin"))
