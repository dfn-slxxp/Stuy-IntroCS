rot13_code = bytes.maketrans(
    b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    b"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")

def rot13():
    string = input("Input something idk\n")
    string_bytes = bytes(string, "utf-8")

    rot13_bytes = string_bytes.translate(rot13_code)

    rot13_string = str(rot13_bytes, encoding="utf-8")

    print(rot13_string)

rot13()