from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()

    answers = []

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                answers.append([nums[i],nums[left],nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return answers

print(three_sum([-1,0,1,2,-1,-4]))
print(three_sum([0,1,1]))
print(three_sum([0,0,0]))
