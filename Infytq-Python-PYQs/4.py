# Input:
# Take a string as an input, separate all the integers from it, Then take each integer only once and form a largest even number possible. 
# Print largest even number possible and if the number can't be made, then print -1

# Test Case 1: asdf@75483   ->  Output: 87534
# Test Case 2: infytq351739 ->  Output: -1

def solve4(sentence):
    
    numList = []
    for letter in sentence:
        if letter.isdigit() and letter not in numList:    numList.append(int(letter))           # numList = [7, 5, 4, 8, 3]
        
    count = 0
    for i in range(0, len(numList)):
        if numList[i] % 2 != 0:  count = count + 1

    if count == len(numList): print(-1)                                                      
    
    else:
        largestEven, smallestEven = -100, 10000000
        
        for i in range(0, len(numList)):
            if numList[i] > largestEven and numList[i] % 2 == 0:    largestEven = numList[i]    # largestEven = 8
            if numList[i] < smallestEven and numList[i] % 2 == 0:   smallestEven = numList[i]   # smallestEven = 4
        
        numList.remove(largestEven)                                                             # numList = [7, 5, 4, 3]
        numList.remove(smallestEven)                                                            # numList = [7, 5, 3]
        
        ans = ""
        ans = ans + str(largestEven)                                                            # ans = "8"
        
        numList.sort(reverse = True)                                                            # numList = [7, 5, 3]
        final = list(map(str, numList))                                                         # numList = ["7", "5", "3"]
        ans = ans + "".join(final)                                                              # final = "8753"

        ans = ans + str(smallestEven)                                                           # final = "87534"    
        
        print(ans)

sentence = "infytq351739"
solve4(sentence)