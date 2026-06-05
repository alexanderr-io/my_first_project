def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


# Check if "Racecar" is a palindrome
print(is_palindrome("Racecar"))

# Check if "Hello" is a palindrome
print(is_palindrome("Hello"))
