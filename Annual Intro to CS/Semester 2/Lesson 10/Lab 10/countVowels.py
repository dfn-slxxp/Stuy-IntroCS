def countVowels(s):
    count = 0
    for char in s:
        count += 1 if char.lower() in ["a", "e", "i", "o", "u"] else 0
    return count
