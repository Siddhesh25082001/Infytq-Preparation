def ans(numList):
    
    if len(numList) < 2:
        return len(numList)
    else:
        i = 0
        for j in range(1, len(numList)):
            
            if numList[j] == numList[i]:
                continue
            else:
                i = i + 1
                numList[i] = numList[j]
      
    return i + 1, numList[:i + 1]
    
numList = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
print(ans(numList))