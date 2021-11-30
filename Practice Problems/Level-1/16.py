#lex_auth_0127136291543285761194

def list_of_count(word_list):
    
    #start writing your code here
    count_list = []
    for word in word_list:
        count_list.append(len(word))
    
    return count_list

word_list = ["Come", "here"]
print(list_of_count(word_list))