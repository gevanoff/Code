def normal_string(string):
    string = string.lower()
    string = string.replace(" ","")
    lst = list(string)
    lst.sort()
    ordered_string = "".join(lst)
    return ordered_string

def is_anagram(s1,s2):
    list1 = normal_string(s1)
    list2 = normal_string(s2)
    
    if list1 == list2:
        return True
    else:
        return False

def anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    return sorted(s1) == sorted(s2)

def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    # Edge Case Check
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    for k in count:
        if count[k] != 0:
            return False
    
    return True
