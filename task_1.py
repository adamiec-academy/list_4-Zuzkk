def is_palindrome(text):
    new_text = text.lower()
    new_text = "".join(new_text.split())
    return new_text == new_text[::-1]
