import unittest

from is_anagram import is_anagram, is_anagram2

class TestIsAnagram(unittest.TestCase):

    def test_basic_anagrams(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("anagram", "nagaram"))
        self.assertTrue(is_anagram("Debit card", "Bad credit"))

    def test_non_anagrams_different_lengths(self):
        self.assertFalse(is_anagram("hello", "hell"))
        self.assertFalse(is_anagram("a", ""))

    def test_non_anagrams_same_length(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("aabbc", "abcde"))
        self.assertFalse(is_anagram("rat", "car"))

    def test_empty_strings(self):
        self.assertTrue(is_anagram("", ""))

    def test_single_character_strings(self):
        self.assertTrue(is_anagram("a", "a"))
        self.assertFalse(is_anagram("a", "b"))

    def test_strings_with_repeated_characters(self):
        self.assertTrue(is_anagram("aabbcc", "abcabc"))
        self.assertTrue(is_anagram("banana", "aananb"))
        self.assertFalse(is_anagram("aabbc", "aaabb"))

    def test_case_sensitivity(self):
        self.assertTrue(is_anagram("Race", "care"))
        self.assertTrue(is_anagram("Hello", "hello"))

    def test_with_spaces_and_punctuation(self):
        self.assertFalse(is_anagram("listen ", "silent"))
        self.assertFalse(is_anagram("hello!", "olleh"))
        self.assertTrue(is_anagram("a b c", "c b a"))


    def test_basic_anagrams_sorted(self):
        self.assertTrue(is_anagram2("listen", "silent"))

    def test_non_anagrams_different_lengths_sorted(self):
        self.assertFalse(is_anagram2("hello", "hell"))


# This allows you to run the tests directly from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
