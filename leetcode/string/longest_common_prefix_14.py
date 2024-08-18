from typing import List

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

    if len(strs) == 1:
        return strs[0]

    f_p = 1
    s_p = 2
    result = commonPrefix(strs[0], strs[1])

    while s_p <= len(strs) - 1:
        current_prefix = commonPrefix(strs[f_p], strs[s_p])
        if not current_prefix:
            return current_prefix

        if len(current_prefix) <= len(result):
            result = current_prefix

        f_p += 1
        s_p += 1
    return result


test_cases = (
    (["flower","flow","flight"], "fl"),
    ([], ""),
    (["dog","racecar","car"], ""),
    (["aaa","aa","aaa"], "aa")
)

for case, expected in test_cases:
    assert longestCommonPrefix(case) == expected, f"Expected: {expected}, actual: {longestCommonPrefix(case)}"