def ans(s):
    
    subString = ""
    l = []
    i, j = 0, 0
    
    while(i < len(s) and j < len(s)):
        if s[j] not in subString:
            subString = subString + s[j]
            j = j + 1
        else:
            l.append(len(subString))
            subString = ""
            i = i + 1
            j = i
    
    l.append(len(subString))
    return max(l)

s = "abcabcbb"
print(ans(s))