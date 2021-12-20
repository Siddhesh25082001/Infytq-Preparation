# Input:
# Take the input from the user in the given format (consist of name and code)
# Find the maximum digit from code which is less than or equal to (<=) the length of name and put the place char in the final string
# If there is not any digit found which satisifies the given condition, then simply put 'X'

# Test Case 1: "Anchal:23581,Aman:57568,Sonakshi:34848,Ria:14585"   ->  Output: aXiR
# Test Case 2: "Sonakshi:34848,Naman:4739,Prachi:2949,Ekta:9889"    ->  Output: iacX

def solve6(sentence):
    
    temp = sentence.split(",")
    
    names, numList = [], []
    for element in temp:
        names.append(element.split(":")[0])
        numList.append(element.split(":")[1])
        
    ans = ""
    k = 0
    for i in range(0, len(numList)):
        
        largest = -100
        for j in range(0, len(numList[i])):
            if int(numList[i][j]) <= len(names[i]) and int(numList[i][j]) >= largest:
                largest = int(numList[i][j])
             
        if largest == -100: ans = ans + 'X'
        else: ans = ans + names[k][largest - 1]
        k = k + 1
        
    return ans
                
sentence = "Sonakshi:34848,Naman:4739,Prachi:2949,Ekta:9889"
print(solve6(sentence))