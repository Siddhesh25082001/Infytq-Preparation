#lex_auth_0127136084107673601177

def rotate_list(input_list, n):
    
    #start writing your code here
    temp = 0
    while n > 0:
        temp = input_list[len(input_list) - 1]
        for i in range(len(input_list) - 1, -1, -1):
            input_list[i] = input_list[i - 1]
        
        input_list[0] = temp
        n = n - 1
    
    return input_list

input_list = [1, 2, 3, 4, 5, 6]
output_list = rotate_list(input_list, 4)
print(output_list)