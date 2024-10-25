"""
Test suite for Teach2Give Technical Test Solutions
------------------------------------------------
Author: Collins Nduhiu
Date: October 25, 2024
"""

import unittest
from solutions import (
    is_palindrome,
    is_pangram,
    reverse_integer,
    capitalize_words
)

class TestPalindrome(unittest.TestCase):
    """Test cases for palindrome checker"""
    
    def test_basic_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
    
    def test_palindrome_phrases(self):
        self.assertTrue(is_palindrome("nurses run"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
    
    def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))  # Empty string
        self.assertTrue(is_palindrome("a"))  # Single character
        self.assertFalse(is_palindrome("ab"))  # Two different characters

class TestPangram(unittest.TestCase):
    """Test cases for pangram checker"""
    
    def test_valid_pangram(self):
        self.assertTrue(is_pangram("The quick brown fox jumps over the lazy dog"))
    
    def test_invalid_pangram(self):
        self.assertFalse(is_pangram("The quick brown fox jumps"))
    
    def test_edge_cases(self):
        self.assertFalse(is_pangram(""))  # Empty string
        self.assertTrue(is_pangram("abcdefghijklmnopqrstuvwxyz"))  # Exact alphabet

class TestIntegerReversal(unittest.TestCase):
    """Test cases for integer reversal"""
    
    def test_basic_reversal(self):
        self.assertEqual(reverse_integer(500), 5)
        self.assertEqual(reverse_integer(91), 19)
    
    def test_negative_numbers(self):
        self.assertEqual(reverse_integer(-56), -65)
        self.assertEqual(reverse_integer(-90), -9)
    
    def test_edge_cases(self):
        self.assertEqual(reverse_integer(0), 0)
        self.assertEqual(reverse_integer(1000), 1)

class TestWordCapitalization(unittest.TestCase):
    """Test cases for word capitalization"""
    
    def test_basic_capitalization(self):
        self.assertEqual(capitalize_words("hi"), "Hi")
        self.assertEqual(capitalize_words("i love programming"), "I Love Programming")
    
    def test_edge_cases(self):
        self.assertEqual(capitalize_words(""), "")
        self.assertEqual(capitalize_words("already MIXED CaSe"), "Already Mixed Case")

if __name__ == '__main__':
    unittest.main()