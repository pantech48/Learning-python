def isValid(s: str) -> bool:
    stack = []

    pairs = {key: value for key, value in zip("([{", ")]}")}

    for sign in s:
        if stack:
            if pairs.get(stack[len(stack)-1]) == sign:
                stack.pop()
                continue
        stack.append(sign)

    return not stack

print(isValid("({[)"))
print(isValid("()[]{}"))
print(isValid("(){}}{"))
print(isValid("(])"))


