# [5, 4, 3, 6, 7, 1, 0]
def min_product(arr):
    if len(arr) < 2:
        raise ValueError("Array should contain at least two elements")

    min1 = min2 = float('inf')
    max1 = max2 = float('-inf')

    for num in arr:
        if num <= min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

        if num >= max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num


    candidates = [
        min1 * min2,
        max1 * max2,
        min1 * max1
    ]

    return min(c for c in candidates if c != float('inf') and c != float('-inf'))



# Тестовые случаи
test_cases = [
    # Положительные числа
    ([2, 3, 5, 7, 11], 6),
    ([1, 2, 3, 4, 5], 2),
    ([10, 20, 30, 40, 50], 200),

    # Отрицательные числа
    ([-1, -2, -3, -4, -5], 2),
    ([-10, -5, -2, -1], 2),

    # Смешанные положительные и отрицательные
    ([-1, 2, -3, 4, -5], -20),
    ([1, -2, 3, -4, 5], -20),

    # Включая нули
    ([0, 1, 2, 3], 0),
    ([-1, 0, 1], -1),
    ([0, 0, 1, 2], 0),

    # Повторяющиеся числа
    ([1, 1, 2, 2, 3], 1),
    ([-2, -2, -2, 1], -4),

    # Граничные случаи
    ([1, 2], 2),
    ([-1, -1], 1),
    ([100, 101], 10100),
    ([-100, 100], -10000),

    # Большие числа
    ([10 ** 9, 10 ** 9 + 1], 10 ** 18 + 10 ** 9),

    # Очень маленькие положительные числа
    ([0.1, 0.2, 0.3], 0.02),
]

for i, (input_nums, expected_output) in enumerate(test_cases):
    result = min_product(input_nums)
    print(f"Тестовый случай {i + 1}:")
    print(f"Вход: {input_nums}")
    print(f"Ожидаемый выход: {expected_output}")
    print(f"Ваш выход: {result}")
    print(f"{'Пройден' if result == expected_output else 'Не пройден'}\n")