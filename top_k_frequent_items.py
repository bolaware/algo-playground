from typing import List
from collections import Counter

# O(N logN) time complexity but can be O(N) with bucket sort
def top_k_frequent_items(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    most_common = counter.most_common(k)
    return [item[0] for item in most_common]


print(top_k_frequent_items([1,2,2,3,3,3], 2))
print(top_k_frequent_items([7,7], 1))
print(top_k_frequent_items([1,1,1,2,2,3], 2))