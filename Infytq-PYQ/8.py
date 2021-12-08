def solve8(sentence8, m):
    prefix = []
    suffix = []
    j = 0
    maxLength = -1
    
    if len(sentence8) % 2 == 0:
        middle = len(sentence8) // 2
        
        while(j < middle):
            prefix.append(sentence8[:j+1])
            j = j + 1
        
        j = middle
        while(j < len(sentence8)):
            suffix.append(sentence8[j:])
            j = j + 1
    
    else:
        middle = len(sentence8) // 2
        
        while(j < middle):
            prefix.append(sentence8[:j+1])
            j = j + 1
        
        j = middle + 1
        while(j < len(sentence8)):
            suffix.append(sentence8[j:])
            j = j + 1
            
    for pr in prefix:
        if pr in suffix and len(pr) > maxLength:
            maxLength = len(pr)
            
    return maxLength

sentence8 = "kkkkk"
print(solve8(sentence8))