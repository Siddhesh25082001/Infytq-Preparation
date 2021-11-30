#lex_auth_01269444195664691284

vowels = ['a', 'e', 'i', 'o', 'u']
def encrypt_sentence(sentence):
    
    #start writing your code here
    l = []
    for word in sentence:
        l = sentence.split(" ")
   
    data = []
    for index, word in enumerate(l):
        if (index + 1) % 2 != 0:
            data.append(word[::-1])
        else:
            vowel = []
            consonant = []
            
            for element in word:
                if element in vowels:
                    vowel.append(element)
                else:
                    consonant.append(element)
                    
            consonant.extend(vowel)
            data.append("".join(consonant))
                
    return " ".join(data)

sentence = "The sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)