#lex_auth_0127136209566679041189

def check_numbers(num1, num2):
    
    #start writing your code here
    num_list = []
    for i in range(num1, num2 + 1):
        for num in range(num1, num2 + 1):
            if i % num == 0 and i != num: num_list.append(i)
            else: continue
        
    # num_list = [i for num in range(num1, num2 + 1) if i % num == 0]
    num_list = set(num_list)
    count = len(num_list)
    return [num_list, count]

num1 = 2
num2 = 20
print(check_numbers(num1, num2))