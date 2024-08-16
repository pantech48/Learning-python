def isPalindrome(s: str) -> bool:
    first_pointer, second_pointer, count = 0, -1, 0
    s = s.strip()

    while count < len(s)/2:
        if not s[first_pointer].isalnum() and not s[second_pointer].isalnum():
            first_pointer += 1
            second_pointer -= 1
            count += 1
        elif not s[first_pointer].isalnum():
            first_pointer += 1
            continue
        elif not s[second_pointer].isalnum():
            second_pointer -= 1
            continue
        if s[first_pointer].lower() != s[second_pointer].lower():
            return False
        first_pointer += 1
        second_pointer -= 1
        count += 1
    return True

print(bool(""))
print(isPalindrome(" "))