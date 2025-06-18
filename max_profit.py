from typing import List

def max_profit(prices: List[int]) -> int:
    max_gain = 0
    min_val = prices[0]

    for price in prices:
        if price < min_val:
            min_val = price
        else:
            max_gain = max(max_gain, price - min_val)

    return max_gain

print(max_profit([10,1,5,6,7,1]))
print(max_profit([10,8,7,5,2]))
print(max_profit([7,1,5,3,6,4]))



"""
[10,1,5,6,7,1]
diff = -9, next_iter = 4, max = 4
i = 1, j = 3, 
diff = 5, next_iter = 1, max = 5
i = 1, j = 4
diff = 6, next_iter = -6, max = 6
i = 1, j = 5
diff = 0, next_iter = 


[10,8,7,5,2]
diff = -2, next_iter = -1, max = -1
i = 1, j = 3
diff = -3, next_iter = -3, max = -1

"""



