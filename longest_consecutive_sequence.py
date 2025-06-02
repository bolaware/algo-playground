from typing import List

def longest_consecutive_sequence(nums: List[int]) -> int:
    num_set = set(nums)
    max_count = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num + 1
            count = 1

            while current in num_set:
                count += 1
                current += 1

            max_count = max(count, max_count)

    return max_count

print(longest_consecutive_sequence([2,20,4,10,3,4,5]))
print(longest_consecutive_sequence([0,3,2,5,4,6,1,1]))
