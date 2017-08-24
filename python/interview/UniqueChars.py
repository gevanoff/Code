def uni_char_me(s):
    uniq_set = set(s)
    lst = list(s)
    if len(uniq_set) == len(lst):
        return True
    else:
        return False
    
def uni_char(s):
    return len(set(s)) == len(s)

def uni_char2(s):
    chars = set()
    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True

uni_char_me('goo')
