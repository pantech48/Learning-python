from typing import List
from itertools import takewhile
def commonPrefix(first_str: str, second_str: str) -> str:
    result = []
    if not len(first_str):
        return ""

    min_length = min(len(first_str), len(second_str))

    for i in range(min_length):
        if first_str[i] == second_str[i]:
            result.append(first_str[i])
        else:
            break
    return "".join(result)


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""

    shortest = min(strs, key=len)
    print(list(zip(*strs)))

    for index, char in enumerate(shortest):
        for word in strs:
            if word[index] != char:
                return shortest[:index]

    return shortest


# beautifully pythonic solution
def longestCommonPrefix2(strs: List[str]) -> str:
    return "".join(x[0] for x in takewhile(lambda x: len(set(x)) == 1, zip(*strs)))


test_cases = (
    (["flower","flow","flight"], "fl"),
    ([], ""),
    (["dog","racecar","car"], ""),
    (["aaa","aa","aaa"], "aa")
)

for case, expected in test_cases:
    assert longestCommonPrefix(case) == expected, f"Expected: {expected}, actual: {longestCommonPrefix(case)}"