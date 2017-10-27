def to_roman_numeral(number):
    if number >= 1000:
        division = number / 1000
        modulo = number % 1000
        return division * 'M' + to_roman_numeral(modulo)
    if number >= 100:
        division = number / 100
        modulo = number % 100
        return number_less_than_1400(division) + to_roman_numeral(modulo)
    if number >= 10:
        division = number / 10
        modulo = number % 10
        return number_less_than_140(division) + to_roman_numeral(modulo)
    else:
        return number_less_than_14(number)


def number_less_than_1400(number):
    a = "C"
    b = "D"
    c = "M"
    roman_value = {a: 1, b: 5, c: 10}
    romans = {a: range(0, 4), b: range(4, 9), c: range(9, 14)}
    return calculate(number, roman_value, romans, "C")


def number_less_than_140(number):
    a = "X"
    b = "L"
    c = "C"
    roman_value = {a: 1, b: 5, c: 10}
    romans = {a: range(0, 4), b: range(4, 9), c: range(9, 14)}
    return calculate(number, roman_value, romans, "X")


def number_less_than_14(number):
    a = "0"
    b = "V"
    c = "X"
    roman_value = {a: 0, b: 5, c: 10}
    romans = {a: range(0, 4), b: range(4, 9), c: range(9, 14)}
    return calculate(number, roman_value, romans, "I")


def calculate(number, roman_value, romans, switch):
    for roman, decimal_values in romans.items():
        if number in decimal_values:
            structure_base = [roman]
            break
    # structure_base = ["V"]
    if number == roman_value[roman] - 1:
        structure_base.insert(0, switch)
    else:
        structure_base.append(switch * (number - roman_value[roman]))
    if "0" in structure_base :
        structure_base = [x for x in structure_base if (x != "0")]

    return ''.join(structure_base)

