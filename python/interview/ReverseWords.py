def rev_word_me(s):
    lst = s.split()
    lst.reverse()
    output = " ".join(lst)
    return output

def rev_word(s):
    words = []
    length = len(s)
    spaces = [' ']
    i = 0
    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
        i += 1
    return " ".join(reversed(words))

rev_word_me("Hey there people!")
