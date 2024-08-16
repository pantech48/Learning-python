from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    hash_nums = {}
    for number in nums:
        if number not in hash_nums.keys():
            hash_nums[number] = 1
        else:
            hash_nums[number] += 1

    for value in hash_nums.values():
        if value > 1:
            return True
    return False

# best solution: return len(set(nums)) != len(nums) Here we can use set to get read of duplicates

test_data = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ([], False),
    ([1], False)
]

for value, expected_result in test_data:
    assert containsDuplicate(value) == expected_result
