from typing import List

def search_target_in_rotated_array(nums: List[int], target: int) -> int:
    n = len(nums)
    if n == 1:
        return 0 if nums[0] == target else -1

    left = 0
    right = n - 1
    mid = (right + left)//2

    while left <= right:
        if target == nums[mid]:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1


        mid = (right + left) // 2

    return -1


print(search_target_in_rotated_array([4,5,6,7,0,1,2], 0))
print(search_target_in_rotated_array([4,5,6,7,0,1,2], 3))
print(search_target_in_rotated_array([1], 0))


"""
[11,13,15,17]
15,17


[6,0,1,2,4,5] 
[6,0] -> left = 0, right = 1, mid = 0
[6]

left = 0, right = 6, mid = 3
[7,0,1,2]
left = 3, right = 6, mid = 4
[7, 0]
left = 3, right = 4, mid = 3
left = 3, right = 3, mid = 3
"""