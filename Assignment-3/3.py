#lex_auth_01269441913243238467

def create_largest_number(number_list):

    #remove pass and write your logic here
    number = ""
    number_list.sort(reverse = True)
    for num in number_list:
        number = number + str(num)
        
    return int(number)
    
number_list = [23, 45, 67]
largest_number = create_largest_number(number_list)
print(largest_number)