from collections import Counter, defaultdict

def longest_characters_without_repeating(s: str) -> int:
    char_map = {}
    start_index = 0
    max_length = 0

    for i in range(len(s)):
        if char_map.get(s[i], None) is not None and start_index <= char_map[s[i]]:
            start_index = char_map[s[i]] + 1
        char_map[s[i]] = i
        max_length = max(max_length, (i + 1) - start_index)
    return max_length


print(longest_characters_without_repeating("abba"))
print(longest_characters_without_repeating("abcabcbb"))
print(longest_characters_without_repeating("bbbbb"))
print(longest_characters_without_repeating("pwwkew"))
"""
abba
abcabcbb
bbbb
pwwkew
{a: 1}, max_length = 1, start_index = 0
{a: 0, b: 1} max_length = 2, start_index = 0
{a: 0, b: 1, c: 2} max_length = 3, start_index = 0
{a: 3, b: 1, c: 2} max_length = 3, start_index = 1
{a: 3, b: 4, c: 2} max_length = 3, start_index = 2

"""