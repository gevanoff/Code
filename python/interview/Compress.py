def compress_me(s):
    lst = list(s)
    pressed = []
    n = 1
    for i in range(1,len(lst)):
        if lst[i-1] == lst[i]:
            n += 1
        else:
            value = lst[i-1] + str(n)
            pressed.append(value)
            n = 1
    value = lst[i-1] + str(n)
    pressed.append(value)
    
    return "".join(pressed)
    
def compress(s):
    # Run length compression algorithm
    r = ""
    l = len(s)
    if l == 0:
        return ""
    if l == 1:
        return s+"1"
    last = s[0]
    cnt = 1
    i = 1
    
    while i < l:
        if s[i] == s[i-1]:
            cnt +=1
        else:
            r = r +s[i-1] + str(cnt)
            cnt = 1
        i += 1
    r = r + s[i-1] + str(cnt)
    
    return r

compress_me('AAAAABBBBCCCC')
