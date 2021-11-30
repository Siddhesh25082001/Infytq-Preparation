#lex_auth_0127136357873991681201

def exchange_list(number_list):
    
    #start writing your code here
    newList = []
    n = len(number_list)
    n = n // 2
    
    newList.extend(number_list[n:])
    newList = newList[::-1]
    
    newList.extend(number_list[0:n])
    
    number_list = newList
    return number_list
     
number_list = [1, 2, 3, 4, 5, 6]
print(exchange_list(number_list))