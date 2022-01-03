#lex_auth_0127426336682147841449

def check_double(list1, list2):
    
    #write your logic here
    new_list = []
    
    for i in range(0, len(list1)):
        if (list1[i] * 2) in list2: new_list.append(list1[i])
    
    return new_list

#Provide different values for the variables and test your program
list1 = [11, 8, 23, 7, 25, 15]
list2 = [6, 33, 50, 31, 46, 78, 16, 34]
print(check_double(list1, list2))
