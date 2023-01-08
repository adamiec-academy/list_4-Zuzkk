def my_split(text):
    words_list = []
    word = ""
    for letter in text.strip():
        if letter == " " and word:
            words_list.append(word)
            word = ""
        elif letter != " ":
            word += letter
    if word:
        words_list.append(word)
    return words_list
