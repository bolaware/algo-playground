import re

def valid_palindrome(s: str) -> bool:

    cleaned = re.sub("[^a-zA-Z0-9]", "", s).lower()

    i = 0
    j = len(cleaned) - 1

    while i < j:
        if cleaned[i] != cleaned[j]:
            return False
        i += 1
        j -= 1

    return True


print(valid_palindrome("A man, a plan, a canal: Panama"))
print(valid_palindrome("race a car"))
print(valid_palindrome(" "))