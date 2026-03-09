def breakSentence(s):
    words = []
    w = ""
    for char in s:
        if char == " ":
            words.append(w)
            w = ""
        else:
            w = w + char
    if w != "":
        words.append(w)

    return words
    