#lex_auth_0127135838317445121147

def count_digits_letters(sentence):
    
    #start writing your code here
    letterCount, digitCount = 0, 0
    
    for ch in sentence:
        if ch.isdigit():
            digitCount = digitCount + 1
        elif ch.isalpha():
            letterCount = letterCount + 1
        else:
            pass
    
    result_list = []
    result_list.append(letterCount)
    result_list.append(digitCount)
    
    return result_list

sentence = "Infosys Mysore 570027"
print(count_digits_letters(sentence))