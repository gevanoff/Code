def pair_sum(lst, total):
    unique_pairs = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                if lst[i] + lst[j] == total:
                    
                    matching = tuple(sorted([lst[i],lst[j]]))
                    unique_pairs.append(matching)
    
    return len(set(unique_pairs))

def pair_sum2(arr,k):
    if len(arr)<2:
        return
    
    # sets for tracking
    seen = set()
    output = set()
    
    for num in arr:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target), max(num,target)))
    return len(output)

pair_sum([1,3,2,2],4)
