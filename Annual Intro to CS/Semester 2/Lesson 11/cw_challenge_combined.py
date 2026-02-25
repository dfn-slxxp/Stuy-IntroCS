# Classwork

def shiftLetterBy1 (c):
    return chr(ord(c) + 1)

def shiftLetterByN(c, n):
    return chr(ord(c) + n)

def isLowerCase(c):
    return ord(c) >= 97 and ord(c) <= 122

def isDigit(c):
    return ord(c) >= 48 and ord(c) <= 57

def uppercaseLetter(c):
    return chr(ord(c) - 32) if isLowerCase(c) else c

def myUpper(str):
    s = ""

    for c in str:
        s = s + uppercaseLetter(c)

    return s



# Challenge

def alphabeticalSentance(str):
    # Split the sentance into words that are all lowercase
    words = str.lower().split()

    print(*words)


    # Initialize empty list for sorted words
    sorted_words = []

    # Sort the list
    while len(words) > 0:
        # Initialize the first index
        first = 0

        # Check to see if a word exists that comes before the "first" word alphabetically
        for i in range(len(words)):
            if words[first] > words[i]:
                # If such word exists, set "first" to that word
                first = i

        # Remove the word with the index of "first" and add it to sorted list
        sorted_words.append(words.pop(first))

    # Create an empty string to store final result
    final_str = ""

    # Iterate through items in sorted list and add each to the final string
    for word in sorted_words:
        final_str = final_str + word + " "

    # Return the result
    return final_str