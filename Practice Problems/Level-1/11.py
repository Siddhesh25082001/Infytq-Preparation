#lex_auth_0127136021907046401165

def find_upper_and_lower(sentence):
    
    #start writing your code here
    lower, upper = 0, 0
    for ch in sentence:
        if ch.isalpha():
            if ch.islower(): lower = lower + 1
            else: upper = upper + 1
        else:
            continue
        
    result_list = []
    result_list.append(upper)
    result_list.append(lower)
       
    return result_list

sentence = "Welcome to Mysore"
print(find_upper_and_lower(sentence))