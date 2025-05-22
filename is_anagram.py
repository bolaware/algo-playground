from collections import Counter

# is_anagram: use char dict frequency counter approach
# is_anagram2: but it doesn't have to be done manually, can simply use Counter to get char frequency
# is_anagram3: or better still sort the strings in alphabetical order and compare

def is_anagram(s1: str, s2: str) -> bool:
    normalized_s1 = s1.lower()
    normalized_s2 = s2.lower()

    if len(normalized_s1) != len(normalized_s2):
        return False

    char_frequency_count1 = {}
    for char in normalized_s1:
        char_frequency_count1[char] = char_frequency_count1.get(char, 0) + 1

    char_frequency_count2 = {}
    for char in normalized_s2:
        char_frequency_count2[char] = char_frequency_count2.get(char, 0) + 1

    return char_frequency_count1 == char_frequency_count2

def is_anagram2(s1: str, s2: str) -> bool:
    normalized_s1 = s1.lower()
    normalized_s2 = s2.lower()

    if len(normalized_s1) != len(normalized_s2):
        return False

    return Counter(normalized_s1) == Counter(normalized_s2)

def is_anagram3(s1: str, s2: str) -> bool:
    normalized_s1 = s1.lower()
    normalized_s2 = s2.lower()

    if len(normalized_s1) != len(normalized_s2):
        return False

    return sorted(normalized_s1) == sorted(normalized_s2)


print(f"Is 'listen' an anagram of 'silent'? {is_anagram('listen', 'silent')}")
print(f"Is 'anagram' an anagram of 'nagaram'? {is_anagram('anagram', 'nagaram')}")
print(f"Is 'Debit card' an anagram of 'Bad credit'? {is_anagram('Debit card', 'Bad credit')}")
print(f"Is 'hello' an anagram of 'world'? {is_anagram('hello', 'world')}")
print(f"Is 'hello' an anagram of 'hell'? {is_anagram('hello', 'hell')}")
print(f"Is '' an anagram of ''? {is_anagram('', '')}")
print(f"Is 'a' an anagram of 'a'? {is_anagram('a', 'a')}")
print(f"Is 'a' an anagram of 'b'? {is_anagram('a', 'b')}")
print(f"Is 'A man, a plan, a canal: Panama' an anagram of 'Panama: a canal, a plan, a man'? {is_anagram('A man, a plan, a canal: Panama', 'Panama: a canal, a plan, a man')}")
print(f"Is 'Race' an anagram of 'care'? {is_anagram('Race', 'care')}")
print(f"Is 'Hello' an anagram of 'hello'? {is_anagram('Hello', 'hello')}")
print(f"Is 'Eleven plus two' an anagram of 'Twelve plus one'? {is_anagram('Eleven plus two', 'Twelve plus one')}")
print(f"Is 'Python' an anagram of 'Pyhton'? {is_anagram('Python', 'Pyhton')}")
