#lex_auth_0127136518921830401222

def find_target_positions(input_string, target_word):
    
    #Start writing your code here
    target_list = []
    words = input_string.split(" ")
    
    for i in range(0, len(words)):
        if words[i] == target_word:
            target_list.append(i)
            
    return target_list

def find_inverted_index(input_string):
    
    #Start writing your code here
    target_dict = {}
    words = input_string.split(" ")
    
    for i in range(0, len(words)):
        if words[i] not in target_dict:
            target_dict[words[i]] = find_target_positions(input_string, words[i])
        else: continue
    
    return target_dict
    
input_string = "we dont need no education we dont need no thought control no we dont"
result_dict = find_inverted_index(input_string)
print(result_dict)