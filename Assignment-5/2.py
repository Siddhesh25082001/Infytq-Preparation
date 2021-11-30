#lex_auth_0127382164803993601239

#This verification is based on string match.
def even(data):
    
    #Remove pass and write the logic here
    even = []
    
    for num in data:
        if num % 2 == 0:
            even.append(num)
        else:
            continue
        
    return even

def odd(data):

    #Remove pass and write the logic here
    odd = []

    for num in data:
        if num % 2 != 0:
            odd.append(num)
        else:
            continue
        
    return odd

def sum_of_numbers(list_of_num, filter_func = None):
    
    #Remove pass and write the logic here
    if filter_func == None:
        return sum(list_of_num)
    
    elif filter_func == even:
        e = even(list_of_num)
        return sum(e)
        
    elif filter_func == odd:
        o = odd(list_of_num)
        return sum(o)
        
    else:
        pass

sample_data = range(1, 11)
print(sum_of_numbers(sample_data, None))