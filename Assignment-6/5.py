# #lex_auth_01269442545042227276

# One Loop
# def find_ten_substring(num_str):
    
#     #Remove pass and write your logic here
#     i, j, sum = 0, 0, 0
#     pairs = []
    
#     while(i < len(num_str) and j < len(num_str)):
#         sum = sum + int(num_str[j])
        
#         if sum >= 10:
#             pairs.append(num_str[i : j + 1])
#             sum = 0
#             i = i + 1
#             j = i
        
#         else:
#             j = j + 1
            
#     return pairs

# Two Loops
def find_ten_substring(num_str):
    pairs = [] 
    sum = 0
    
    for i in range(0, len(num_str)):
        sum = 0
        
        for j in range(i, len(num_str)):
            sum = sum + int(num_str[j])  
            
            if(sum == 10):
                pairs.append(num_str[i: j + 1])
            
            if(sum > 10):
                break
            
    return pairs
    
num_str="3523014"
print("The number is:", num_str)
result_list = find_ten_substring(num_str)
print(result_list)