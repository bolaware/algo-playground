from collections import Counter, defaultdict
from typing import List


def group_anagram(strs: List[str]) -> List[List[str]]:
    counter_map = defaultdict(list)
    answer = []

    for _str in strs:
        sorted_str = ''.join(sorted(_str)) # or use a tuple counter_key(_str)
        counter_map[sorted_str].append(_str)

    for key, val in counter_map.items():
        answer.append(val)

    return answer

def counter_key(s: str):
    return tuple(sorted(Counter(s).items()))

print(group_anagram(["eat","tea","tan","ate","nat","bat"]))
print(group_anagram([""]))
print(group_anagram(["a"]))