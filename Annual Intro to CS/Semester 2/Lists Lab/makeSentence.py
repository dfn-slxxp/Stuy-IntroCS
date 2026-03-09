def makeSentence(words):
    if len(words) == 0:
        return ""
    if len(words) == 1:
        return words[0]

    w = words[0]
    for word in words[1:]:
        w = w + " " + word

    return w
