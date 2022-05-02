#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in April 2022
# This is the math program, transforming Fahrenheit into Celsius


def fahrenheit():
    # This function transforms temperature's units

    # input
    temperature_Celsius_string = input("Enter a temperature (°C): ")

    # process & output
    print("")
    try:
        temperature_Celsius_integer = int(temperature_Celsius_string)
        temperature_Fahrenheit = (9 / 5) * temperature_Celsius_integer + 32
        print(
            "{0:,.2f}°C is equal to {1:,.2f}°F.".format(
                temperature_Celsius_integer, temperature_Fahrenheit
            )
        )
    except Exception:
        print("Invalid number!")
    finally:
        print("\nDone.")


def main():
    # This function calls out other functions

    # call functions
    fahrenheit()


if __name__ == "__main__":
    main()
