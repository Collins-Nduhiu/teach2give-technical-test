"""
Teach2Give Technical Test Solutions
---------------------------------
Author: [Your Name]
Date: October 22, 2024

This module contains solutions to the Teach2Give technical test questions.
Each solution is documented and includes example usage.
"""

# Question 1: SQL Query
SQL_QUERY = """
SELECT 
    r.race_name,
    c.circuit_location,
    d.driver_name,
    res.grid,
    res.position,
    res.points,
    res.fastest_lap,
    res.race_time as time,
    r.race_year as year,
    con.team as team_name,
    r.race_date as date
FROM races r
JOIN circuits c ON r.circuit_id = c.circuit_id
JOIN results res ON r.race_id = res.race_id
JOIN drivers d ON res.driver_id = d.driver_id
JOIN constructors con ON res.constructor_id = con.constructor_id
WHERE r.race_year = 2020
ORDER BY res.points DESC;
"""
def is_palindrome(text: str) -> bool:
    """
    Question 2: Check if a word or phrase is a palindrome.
    
    Args:
        text (str): Input string to check
        
    Returns:
        bool: True if palindrome, False otherwise
        
    Examples:
        >>> is_palindrome("madam")
        True
        >>> is_palindrome("nurses run")
        True
    """
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]

def is_pangram(text: str) -> bool:
    """
    Question 3: Check if a string is a pangram.
    
    Args:
        text (str): Input string to check
        
    Returns:
        bool: True if pangram, False otherwise
        
    Examples:
        >>> is_pangram("The quick brown fox jumps over the lazy dog")
        True
    """
    unique_letters = {char for char in text.lower() if char.isalpha()}
    return len(unique_letters) == 26

def reverse_integer(number: int) -> int:
    """
    Question 4: Reverse the digits of an integer.
    
    Args:
        number (int): Input integer
        
    Returns:
        int: Integer with reversed digits
        
    Examples:
        >>> reverse_integer(500)
        5
        >>> reverse_integer(-56)
        -65
    """
    sign = -1 if number < 0 else 1
    abs_num = abs(number)
    reversed_num = int(str(abs_num)[::-1])
    return sign * reversed_num

def capitalize_words(text: str) -> str:
    """
    Question 5: Capitalize first letter of each word.
    
    Args:
        text (str): Input string
        
    Returns:
        str: String with capitalized words
        
    Examples:
        >>> capitalize_words("i love programming")
        'I Love Programming'
    """
    return text.title()

if __name__ == "__main__":
    # Quick manual test of each function
    print("Testing palindrome function:")
    print(is_palindrome("madam"))  # True
    
    print("\nTesting pangram function:")
    print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
    
    print("\nTesting integer reversal:")
    print(reverse_integer(500))  # 5
    print(reverse_integer(-56))  # -65
    
    print("\nTesting word capitalization:")
    print(capitalize_words("i love programming"))  # I Love Programming