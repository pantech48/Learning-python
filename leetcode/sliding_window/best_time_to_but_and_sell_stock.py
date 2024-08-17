from typing import List


def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit

test_cases = (
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
    ([], 0),
    ([7, 2, 5, 1, 7], 6)
)

for arg, expected in test_cases:
    assert maxProfit(arg) == expected