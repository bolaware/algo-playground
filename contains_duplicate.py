from typing import List

## initial solution using dict
def contains_duplicate(nums: List[int]) -> bool:
    element_counts = {}
    for num in nums:
        if num in element_counts:
            element_counts[num] += 1
        else:
            element_counts[num] = 1

    for _, value in element_counts.items():
        if value > 1:
            return True
    return False

## better solution using dict
def contains_duplicate2(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

# 2. Call the method with some test data
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 1]
list3 = []
list4 = [7]

# 3. Print the return value of the method to the terminal
print(f"Does {list1} have duplicates? {contains_duplicate(list1)}")
print(f"Does {list2} have duplicates? {contains_duplicate(list2)}")
print(f"Does {list3} have duplicates? {contains_duplicate(list3)}")
print(f"Does {list4} have duplicates? {contains_duplicate(list4)}")
print("------Solution 2-----")
print(f"Does {list1} have duplicates? {contains_duplicate2(list1)}")
print(f"Does {list2} have duplicates? {contains_duplicate2(list2)}")
print(f"Does {list3} have duplicates? {contains_duplicate2(list3)}")
print(f"Does {list4} have duplicates? {contains_duplicate2(list4)}")