def to_roman_numeral(number):
    if number == 0:
        return ""
    for bracket in [1000, 100, 10, 1]:
        if number >= bracket:
            return roman100(number, bracket) + to_roman_numeral(number % bracket)


def roman100(number, bracket):

    roman_brackets = {
        1000: {
            "roman_unit": "M",
            "roman_fiver": "",
            "roman_up": ""
        },
        100: {
            "roman_unit": "C",
            "roman_fiver": "D",
            "roman_up": "M",
        },
        10: {
            "roman_unit": "X",
            "roman_fiver": "L",
            "roman_up": "C",
        },
        1: {
            "roman_unit": "I",
            "roman_fiver": "V",
            "roman_up": "X",
        },
    }

    division = number/bracket
    roman_unit = roman_brackets[bracket]["roman_unit"]
    roman_fiver = roman_brackets[bracket]["roman_fiver"]
    roman_up = roman_brackets[bracket]["roman_up"]

    if division == 9:
        return roman_unit + roman_up
    elif division >= 4:
        if division == 4:
            return roman_unit + roman_fiver
        if division == 5:
            return roman_fiver
        else:
            return roman_fiver + roman_unit * (division - 5)
    else:
        return roman_unit * division
