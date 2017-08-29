def permute(s):
    out = []
    if len(s) == 1:
        out = [s]
    else:
        #for every letter in string
        for i,let in enumerate(s):
            #For every permutation resulting from step 2 and 3
            for perm in permute( s[:i] + s[i+1:]):
                print('letter is', let)
                print('perm is', perm)
                out += [let+perm]
    return out

permute('abc')
