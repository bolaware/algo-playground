from typing import List

def max_area(heights: List[int]) -> int:
    max_a = 0
    i, j = 0, len(heights) - 1

    while i < j:
        min_height = min(heights[i], heights[j])
        max_a = max(min_height * abs(j - i), max_a)

        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    return max_a

print(max_area([1,8,6,2,5,4,8,3,7]))
print(max_area([1,1]))


