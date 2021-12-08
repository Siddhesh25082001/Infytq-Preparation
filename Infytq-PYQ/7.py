def solve7(sentence7):
    items = sentence7.split(",")
    l = []
    
    for item in items:
        l.append(item.split(":")[0])
        l.append(item.split(":")[1])
        
    count = {l[i]: l[i + 1] for i in range(0, len(l), 2)}
    
    for key, value in count.items():
        
        # Sum of sqaures of digits
        s = 0
        for ch in value:
            s = s + int(ch)**2
        count[key] = s
        
        # Updating the key
        str = ""
        if s % 2 == 0:
            str = str +  key[-2:] + key[:-2]
        else:
            str = str + key[1:] + key[0]
        count[str] = count.pop(key)
        
    ans = []
    for key, value in count.items():
        ans.append(key)
    
    return " ".join(ans)

sentence7 = "abcd:1234,bcdgfhf:127836,sdjks:1245"
print(solve7(sentence7))