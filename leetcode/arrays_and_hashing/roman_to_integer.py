def romanToInt(s: str) -> int:
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    first_pointer = 0
    second_pointer = 1
    summ = 0
    while first_pointer <= len(s) - 1:
        if second_pointer == len(s):
            summ += roman_dict[s[first_pointer]]
            break
        if s[first_pointer] == "I" and s[second_pointer] == "V":
            summ += 4
            first_pointer += 2
            second_pointer += 2
        elif s[first_pointer] == "I" and s[second_pointer] == "X":
            summ += 9
            first_pointer += 2
            second_pointer += 2
        elif s[first_pointer] == "X" and s[second_pointer] == "L":
            summ += 40
            first_pointer += 2
            second_pointer += 2
        elif s[first_pointer] == "X" and s[second_pointer] == "C":
            summ += 90
            first_pointer += 2
            second_pointer += 2
        elif s[first_pointer] == "C" and s[second_pointer] == "D":
            summ += 400
            first_pointer += 2
            second_pointer += 2
        elif s[first_pointer] == "C" and s[second_pointer] == "M":
            summ += 900
            first_pointer += 2
            second_pointer += 2
        elif second_pointer == len(s):
            summ += roman_dict[s[first_pointer]]
            summ += roman_dict[s[second_pointer]]
            break
        else:
            summ += roman_dict[s[first_pointer]]
            first_pointer += 1
            second_pointer += 1
    return summ

