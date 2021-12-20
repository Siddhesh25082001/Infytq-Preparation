# Input:
# Take input from the user in the given format (consist of name and code)
# Find the sum of square of digits from code. If the sum of squares of digits of the code are:
#   - Even: Then add the last 2 characters in the beginning
#   - Odd:  Then add first character at the end

# Test Case 1: abcd:1234,bcdgfhf:127836,sdjks:1245      ->      Ouptut: cdab cdgfhfb kssdj

def solve7(sentence):
    
    temp = sentence.split(",")
    
    words, numList = [], []
    for element in temp:
        words.append(element.split(":")[0])
        numList.append(element.split(":")[1])
        
    ans = []
    for i in range(0, len(numList)):
        
        code = 0
        for j in range(0, len(numList[i])):
            code = code + ( int(numList[i][j]) * int(numList[i][j]) )
            
        if (code % 2 == 0):
            ans.append(words[i][-2:] + words[i][:-2])
        else:
            ans.append(words[i][1:] + words[i][0])
            
    return " ".join(ans)

sentence = "abcd:1234,bcdgfhf:127836,sdjks:1245"
print(solve7(sentence))