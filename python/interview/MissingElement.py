def finder(arr1,arr2):
    sorted1 = sorted(arr1)
    sorted2 = sorted(arr2)
    for n in range(len(sorted2)):
        if sorted1[n] != sorted2[n]:
            print("%d is the missing number" % sorted1[n])
            return
    print("%d is the missing number" % sorted1[-1])
    
def finder2(arr1,arr2):
    arr1.sort()
    arr2.sort()
    #zip binds lists together into pairs of matching tuples
    for num1, num2 in zip(arr1,arr2):
        if num1 != num2: #compares num1 and num2 of each tuple
            return num1
    return arr1[-1]

import collections

def finder3(arr1,arr2):
    d = collections.defaultdict(int)
    for num in arr2:
        #would throw an error if key were not already in dict
        #if you didn't use collections
        d[num] += 1 
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1
        
def finder4(arr1,arr2):
    result=0
    #Perform XOR between the numbers in the arrays
    for num in arr1+arr2:
        result^=num
        print(result)
    return result

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
