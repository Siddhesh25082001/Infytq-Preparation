#lex_auth_01269446319507046499

def remove_duplicates(value):
    
    #start writing your code here
    data = []
    for ch in value:
        if ch not in data: data.append(ch)
        
    return "".join(data)

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))