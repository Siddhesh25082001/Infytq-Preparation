def ans(numList, target):
    
    pair = []
    for i in range(0, len(numList)):
        if (target - numList[i] in numList and numList.index(target - numList[i]) != i):
            pair.append(i)
            pair.append(numList.index(target - numList[i]))
            break
        else:
            continue
    
    pair.sort()
    return pair
    
numList = [3, 2, 3]
target = 6

print(ans(numList, target))