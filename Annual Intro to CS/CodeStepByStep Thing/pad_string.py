def pad_string(str, i):
    if i < len(str):
        return str
    else:
        return str + (" " * (i - len(str)))