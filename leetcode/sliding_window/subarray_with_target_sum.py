def sub_arr_with_target_sum(arr, target):
    current_sum = 0
    hash_map = {0: -1}

    for idx, num in enumerate(arr):
        current_sum += num
        if current_sum - target in hash_map:
            return hash_map[current_sum - target] + 1, idx
        hash_map[current_sum] = idx
    return None


def test_sub_arr_with_target_sum(func):
    test_cases = [
        # Базовые случаи
        ([1, 2, 3, 4, 5], 9, (1, 3)),  # Подмассив в середине
        ([1, 2, 3, 4, 5], 15, (0, 4)),  # Весь массив
        ([1, 2, 3, 4, 5], 3, (0, 1)),  # Подмассив в начале
        ([1, 2, 0, 4, 5], 5, (4, 4)),  # Подмассив в конце (одно число)

        # Случаи с отрицательными числами
        ([-1, 2, 3, -4, 5], 5, (1, 2)),  # Подмассив с отрицательными числами
        ([-1, -2, -3, -4, -5], -9, (1, 3)),  # Все отрицательные числа

        # Случаи с нулями
        ([0, 1, 2, 3, 4, 5], 6, (0, 3)),  # Ноль в начале
        ([1, 2, 3, 0, 4, 5], 7, (2, 4)),  # Ноль в середине
        ([0, 0, 0], 0, (0, 0)),  # Все нули, сумма 0

        # Краевые случаи
        ([], 0, None),  # Пустой массив
        ([5], 5, (0, 0)),  # Массив из одного элемента
        ([1, 2, 3], 10, None),  # Сумма не существует

        # Сложные случаи
        ([1, -1, 1, -1, 1, -1, 1], 0, (0, 1)),  # Чередующиеся 1 и -1
        ([1, 2, 3, 4, 5, -15, 1, 2, 3, 4, 5], 15, (0, 4)),  # Два подмассива с одинаковой суммой
        ([1, 1, 1, 1, 1, 1], 3, (0, 2)),  # Несколько подходящих подмассивов

        # Случаи с большими числами
        ([1000000, 1000000, 1000000], 2000000, (0, 1)),  # Большие числа
        ([2 ** 31 - 1, -(2 ** 31), 2 ** 31 - 1], -1, (0, 1))  # Граничные значения int32
    ]

    for i, (arr, target, expected) in enumerate(test_cases, 1):
        result = func(arr, target)
        assert result == expected, f"Test case {i} failed. Expected {expected}, but got {result} for arr={arr}, target={target}"
        print(f"Test case {i} passed!")

# Использование:
test_sub_arr_with_target_sum(sub_arr_with_target_sum)