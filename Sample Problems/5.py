# 1
def solve1(sentence):
    
    words = sentence.split(" ")
    l = []
    
    for word in words:
        newWord = word[::-1]
        l.append(newWord)
        
    return " ".join(l)

# 2
def solve2(sentence):
    
    words = sentence.split()
    l = []
    
    for i in range(0, len(words)):
        if i % 2 != 0:
            newWord = (words[i])[::-1]
            l.append(newWord)
        else:
            l.append(words[i])
        
    return " ".join(l)      

# 3
def solve3(sentence1, sentence2):
    n1 = len(sentence1)
    n2 = len(sentence2)
    
    l = []
    if n1 == n2:
        i, j = 0, 0
        while(i < n1 or j < n2):
            l.append(sentence1[i])
            l.append(sentence2[j])
            i = i + 1
            j = j + 1
    else:
        
        if n1 < n2:
            i, j = 0, 0
            while(i < n1 and j < n1):
                l.append(sentence1[i])
                l.append(sentence2[j])
                i = i + 1
                j = j + 1
            
            l.append(sentence2[j: ])
        
        else:
            i, j = 0, 0
            while(i < n2 and j < n2):
                l.append(sentence1[i])
                l.append(sentence2[j])
                i = i + 1
                j = j + 1
            
            l.append(sentence1[i: ])
    
    return "".join(l)    

# 4
def solve4(sentence3):
    alphabets = []
    digits = []
    
    for letter in sentence3:
        if letter.isalpha(): alphabets.append(letter)
        elif letter.isdigit(): digits.append(letter)
        else: continue
    
    ans = alphabets + digits
    return "".join(ans)

# 5
def solve5(sentence4):
    ans = []
    for i in range(1, len(sentence4), 2):
        ans.append(sentence4[i - 1] * int(sentence4[i]))
    
    return "".join(ans)    

# 6
def solve6(sentence4):
    ans = []
    
    for letter in range(0, len(sentence4)):
        if letter % 2 == 0:
            ans.append(sentence4[letter])
        else:
            ans.append(chr(ord(sentence4[letter - 1]) + int(sentence4[letter])))
            
    return "".join(ans)

# 7
def solve7(sentence5):
    
    sentence5 = list(sentence5)
    if len(sentence5) < 2:
        return sentence5
    else:
        i = 0;
        for j in range(1, len(sentence5)):
            if sentence5[j] == sentence5[i]: continue
            else:
                i = i + 1;
                sentence5[i] = sentence5[j]
                
    return "".join(sentence5[:i+1])
    
# 8.a -> Using Dictionary
def solve8a(sentence6):
    
    count = dict()
    ans = ""
    
    for letter in sentence6:
        if letter in count: count[letter] = count[letter] + 1
        else: count[letter] = 1
        
    for key, value in count.items():
        ans = ans + key + str(value)
        
    return ans
          
# 8.b -> Not Using Dictionary
def solve8b(sentence6):
    
    ans = ""
    for letter in sentence6:
        if letter not in ans:
            ans = ans + letter
            ans = ans + str(sentence6.count(letter))
            
    return ans
        
sentence = "how are you siddhesh"
sentence1 = "mane"
sentence2 = "siddhesh"
sentence3 = "S1iddhesh2mane3"
sentence4 = "a4b3c1"
sentence5 = "0112223333"
sentence6 = "aaaabbbc"

print(solve1(sentence))
print(solve2(sentence))
print(solve3(sentence1, sentence2))
print(solve4(sentence3))
print(solve5(sentence4))
print(solve6(sentence4))
print(solve7(sentence5))
print(solve8a(sentence6))
print(solve8b(sentence6))
