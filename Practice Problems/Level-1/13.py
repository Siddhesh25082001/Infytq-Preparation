#lex_auth_0127136075580375041172

def check_22(num_list):
    
    #start writing your code here
    flag = False
    for num in range(0, len(num_list) - 1):
        if num_list[num] == 2 and num_list[num + 1] == 2: 
            flag = True
            return True
        else: 
            continue
        
    if not flag: return False
        
print(check_22([3, 2, 5, 1, 2, 1, 2, 2]))