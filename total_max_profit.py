from typing import List

def total_max_profit(prices: List[int]) -> int:
    profits = []

    for i in range(len(prices)):
        price = prices[i]
        if i != 0 and price > prices[i - 1]:
            curr_max = price - prices[i - 1]
            profits.append(curr_max)


    max_profit = 0
    for profit in profits:
        max_profit += profit

    return max_profit

print(total_max_profit([7,1,5,3,6,4]))
print(total_max_profit([1,2,3,4,5]))
print(total_max_profit([7,6,4,3,1]))

