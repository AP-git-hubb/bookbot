def count_words(s):
    return len(s.split())

def count_letters(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0,
    }

    for l in s.lower():
        if l in alphabet:
            letters[l] += 1
    return letters

def sort_on(items):
    return items["num"]

def sort_dict(d):
    listed_dict = []
    for letter in d:
        new_dict = {}
        new_dict["char"] = letter
        new_dict["num"] = d[letter]
        listed_dict.append(new_dict)
    
    listed_dict.sort(reverse=True, key=sort_on)
    return listed_dict
