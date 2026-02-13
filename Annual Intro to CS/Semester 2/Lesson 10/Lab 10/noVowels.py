def noVowels(s):
    st = ""
    for char in s:
        if not char.lower() in ["a", "e", "i", "o", "u"]:
            st = st + char

    return st
