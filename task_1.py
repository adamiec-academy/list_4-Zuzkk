def is_palindrome(text):
    new_text = ""
    lower_text = text.lower()
    text_list = lower_text.split()
    new_text = "".join(text_list)
    return new_text == new_text[::-1]
