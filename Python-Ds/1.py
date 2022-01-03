#lex_auth_0127426166978887681375

def merge_list(list1, list2):
    
    #write your logic here
    merged_data = ""
    list2 = list2[::-1]
    
    for i in range(0, len(list1)):
        
        if(list1[i] != None and list2[i] != None):
            merged_data = merged_data + list1[i] + list2[i]
        elif(list1[i] == None):
            merged_data = merged_data + list2[i]
        elif(list2[i] == None):
            merged_data = merged_data + list1[i]
        
        merged_data = merged_data + " "
     
    return merged_data[:-1]

#Provide different values for the variables and test your program
list1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2 = ['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']
merged_data = merge_list(list1,list2)
print(merged_data)
