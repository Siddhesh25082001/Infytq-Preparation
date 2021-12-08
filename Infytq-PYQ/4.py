def solve4(sentence4):
    
    if "0" not in sentence4 or "2" not in sentence4 or "4" not in sentence4 or "6" not in sentence4 or "8" not in sentence4:
        return -1
    else:
        numList = []
        smallestEven, largestEven = 100000, 0
        
        for ch in sentence4:
            if ch.isdigit(): numList.append(ch)
            else: continue
        
        numList = list(map(int, numList))
        
        for num in numList:
            if num % 2 == 0:
                if num < smallestEven: smallestEven = num
                if num > largestEven: largestEven = num
    
        numList.remove(smallestEven)
        numList.remove(largestEven)
        numList.sort(reverse = True)
        
        ans = []
        ans.append(largestEven)
        ans.extend(numList)
        ans.append(smallestEven)
    
        return "".join(list(map(str, ans)))

sentence4 = "google08264"
print(solve4(sentence4))