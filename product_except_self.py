from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    output = [1] * n
    product = 1

    for index in range(len(nums)):
        output[index] = product
        product = product * nums[index]

    product = 1
    for index in range(len(nums) - 1, -1, -1):
        output[index] = product * output[index]
        product = product * nums[index]

    return output


print(product_except_self([1,2,4,6]))
print(product_except_self([-1,0,1,2,3]))