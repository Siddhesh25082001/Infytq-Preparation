#lex_auth_0127382206342184961397

def check_anagram(data1,data2):
    #start writing your code here
    data1 = data1.lower()
    data2 = data2.lower()
    
    if len(data1) == len(data2):
        count = 0
        for i in range(len(data2)):
            if data1[i] in data2 and data2[i] in data1 and data1[i] != data2[i]:
                count += 1
            else:
                return False
        
        if count == len(data1):
            return True
        else:
            return False
    else:
        return False

print(check_anagram("eat","tea"))