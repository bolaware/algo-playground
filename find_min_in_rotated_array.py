from typing import List

"""
[4,5,6,7,0,1,2]
[0,1,2]
[0,1]
"""
def find_min(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    left = 0
    right = n - 1
    mid = (left + right)//2
    while left < right:
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
        mid = (left + right)//2
    return nums[mid]




print(find_min([3,4,5,1,2]))
print(find_min([11,13,15,17]))
print(find_min([4,5,6,7,0,1,2]))