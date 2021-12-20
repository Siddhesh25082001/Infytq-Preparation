# Input:
# Given a string s, find the length of the longest prefix which is also a suffix. 
# The prefix and suffix should not be overlap

# Test Case 1: abcdabc      ->      Output: 3
# Test Case 2: ababa        ->      Output: 1

def solve8(sentence):
    
    prefix, suffix = [], []
    maxLength = 0
    
    if len(sentence) == 1: return len(sentence)
    
    elif len(sentence) == 2:
        
        # Prefix will be first element and combination of first and second
        prefix.append(sentence[0:1])
        prefix.append(sentence[0:])

        # Suffix will be second element and combination of first and second
        suffix.append(sentence[-1:])
        suffix.append(sentence[0:])
        
        for i in range(0, len(prefix)):
            if prefix[i] == suffix[i] and len(prefix[i]) > maxLength:
                maxLength = len(prefix[i])
            
        return maxLength
    
    else:
    
        # Finding all the prefixes
        for p in range(0, len(sentence) // 2):
            prefix.append(sentence[0: p+1])
            
        # Finding all the suffixes
        for s in range((len(sentence) - 1), len(sentence) // 2, -1):
            suffix.append(sentence[s: len(sentence)])
            
        for i in range(0, len(prefix)):
            if prefix[i] == suffix[i] and len(prefix[i]) > maxLength:
                maxLength = len(prefix[i])
                
        return maxLength
                
sentence = "abcdabc"
print(solve8(sentence))