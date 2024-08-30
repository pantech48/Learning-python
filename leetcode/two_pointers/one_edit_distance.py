def one_edit_distance(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) > len(s2):
        s1, s2 = s2, s1

    diff = 0
    f, s = 0, 0

    while f < len(s1) and s < len(s2):
        if s1[f] != s2[s]:
            diff += 1
            if diff > 1:
                return False
            if len(s1) == len(s2):
                f += 1
            s += 1
        else:
            f += 1
            s += 1
    if s < len(s2):
        diff += 1
    print(f" s1 = {s1}, s2 = {s2}, diff = {diff}")
    return True if diff == 0 else diff == 1



test_cases = (
    (('ca', 'catt'), False),
    (('cat', 'cut'), True),
    (('ca', 'cat'), True),
    (('cat', 'ca'), True),
    (('ananan', 'anasan'), True),
    (('catro', 'cat'), False),
    (('casa', 'catu'), False),
    (('ananan', 'anasana'), False),
    (('abfgh', 'abgh'), True),
    (('abgh', 'abfgh'), True),
    (('abgh', 'abfghas'), False),
    (('', 'c'), True),

)

for args, expected in test_cases:
    assert one_edit_distance(*args) == expected, f"{one_edit_distance(*args)} != {expected} for args {args}"