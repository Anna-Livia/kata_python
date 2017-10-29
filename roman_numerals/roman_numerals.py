def to_roman_numeral(number):
    decimal_to_romans = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    romans = ["I", "V", "X", "L", "C", "D", "M"]
    if number in decimal_to_romans:
        return decimal_to_romans[number]
    elif number + 1 in decimal_to_romans:
        switch_index = romans.index(decimal_to_romans[number + 1]) - 1
        switch = romans[switch_index]
        return switch + decimal_to_romans[number]

print to_roman_numeral(4)
