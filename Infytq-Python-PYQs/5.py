# Input:
# A non empty string input_str containing only brackets '(', '[', '{', ')', ']', '}'
# Return Output as 0 if brackets are properly nested
# Return Output position of element + 1 index in input_str which is not properly nested

# Test Case 1: {([])}[]     ->      Output: 0
# Test Case 2: {{[]}}}      ->      Output: 7
# Test Case 3: {([])][]     ->      Output: 6

def solve5(sentence):
    
    stack = []
    for i in range(0, len(sentence)):
        
        if sentence[i] == '(' or sentence[i] == '[' or sentence[i] == '{':   stack.append(sentence[i])
        else:
            if (len(stack) == 0):   return i+1
            else:
                x = stack.pop()
                if(sentence[i] == ')' and x != '('):    return i+1
                elif(sentence[i] == ']' and x != '['):  return i+1
                elif(sentence[i] == '}' and x != '{'):  return i+1
                else: continue

    return 0

sentence = "{([])][]"
print(solve5(sentence))