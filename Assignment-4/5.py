#lex_auth_01269444961482342489

def sms_encoding(data):
    
    #start writing your code here
    words = data.split()
    vowels = "aeiouAEIOU"
    sentence = ""
    
    for word in words:
        
        if(len(word) == 1):
            sentence = sentence + word
        
        else:
            for letter in word:
                if letter not in set(vowels):
                    sentence = sentence + letter
        
        sentence = sentence + " "
    
    return sentence[0:-1]

data = "I love Python"
print(sms_encoding(data))