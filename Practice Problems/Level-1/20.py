#lex_auth_0127136332814499841204

def sum_of_elements(num_list, number):
    
    result_sum = 0
    num = 0

    while(num < len(num_list)):
        
        if num_list[num] == number and num == 0:
            result_sum = result_sum
            
            if num + 1 >= len(num_list): break
            else:
                num_list[num + 1] = result_sum

            num = num + 2

        elif num_list[num] == number:
            result_sum = result_sum - num_list[num - 1]
            
            if num + 1 >= len(num_list): break
            else:
                num_list[num + 1] = result_sum

            num = num + 2

            
        else:
            result_sum = result_sum + num_list[num]
            num = num + 1
        
    return result_sum
      
num_list = [2, 3, 4, 5, 6, 2, 3]
number = 2
print(sum_of_elements(num_list, number))