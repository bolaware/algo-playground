from collections import Counter, defaultdict


def longest_characters_without_repeating_with_replacement(s: str, k: int) -> int:
    i, j, max_length = 0, 1, 0
    frequency_counter = defaultdict(int)
    max_counter = 0
    for j in range(len(s)):
        frequency_counter[s[j]] += 1
        max_counter = max(max_counter, frequency_counter[s[j]])
        if (j + 1 - i) - max_counter <= k:
            max_length = max(max_length, j + 1 - i)
        else:
            frequency_counter[s[i]] -= 1
            i += 1
    return max_length


print(longest_characters_without_repeating_with_replacement("ABAB", 2))
print(longest_characters_without_repeating_with_replacement("AABABBA", 1))

