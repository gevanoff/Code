def large_cont_sum_me(arr):
    fwd_sum = bwd_sum = 0
    fwd_ele = bwd_ele = ""
    for i in range(len(arr)):
        n = sum(arr[0:i])
        if n >= fwd_sum:
            fwd_sum = n
            fwd_ele = i
    for i in range(len(arr)):
        n = sum(arr[i:len(arr)])
        if n >= bwd_sum:
            bwd_sum = n
            bwd_ele = i
    return sum(arr[bwd_ele:fwd_ele])

def large_cont_sum(arr):
    if len(arr)==0:
        return 0
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum+num,num)
        max_sum = max(current_sum,max_sum)
    return max_sum

large_cont_sum_me([1,2,-1,3,4,10,10,-10,-1])
