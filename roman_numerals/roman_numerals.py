def loaded():
    return True


def to_roman_numeral(number):
    if number <= 3:
        return number * "I"
    elif number <= 5:
        if number < 5:
            return "IV"
        else:
            return "V"

