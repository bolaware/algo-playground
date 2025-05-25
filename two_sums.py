from typing import List

def two_sums(target: int, nums: List[int]) -> list[int]:
    compliments = {}
    answer = []
    for index, num in enumerate(nums):
        if num in compliments:
            answer.append(compliments[num])
            answer.append(index)
            return answer
        else:
            compliments[target - num] = index

    return answer

print(two_sums(10, [5,5]))
