# Write a Python function that checks whether
# a given string is a palindrome. A palindrome
# is a word, phrase, or sequence that reads the
# same backward as forward (e.g., "madam" or
# "racecar").

def palindrome(text):
    original=text
    return text[::-1]==original

text=input("Enter String:-")
print(palindrome(text))