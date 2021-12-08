def solve12(sentence12):
    
    specialCharacter = []
    even = []
    odd = []
    
    for ch in sentence12:
        if ch.isdigit():
            if int(ch) % 2 == 0: even.append(ch)
            else: odd.append(ch)
        elif ch.isalpha(): continue
        else: specialCharacter.append(ch)
      
    ans = []
    if len(specialCharacter) % 2 == 0:
        ans = zip(even, odd)
    else:
        ans = zip(odd, even)
        
    ans = out = [item for t in ans for item in t]
    
    if len(even) > len(odd):
        ans.extend(even[len(odd):])
    elif len(odd) > len(even):
        ans.extend(odd[len(even):])
    else: 
        pass
    
    return "".join(ans)

sentence12 = "A567r21i@p#8t"
numList = [3, 2, 5, 8, 9, 10, 11]
print(solve12(sentence12))