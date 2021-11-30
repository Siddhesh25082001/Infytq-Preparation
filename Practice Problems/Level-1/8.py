#lex_auth_0127135929511936001157

def calculate_net_amount(trans_list):
    
    #start writing your code here
    deposit,  withDraw = 0, 0
    for element in trans_list:
        if element[0] == 'D':
            deposit = deposit + int(element[2:])
        elif element[0] == 'W':
            withDraw = withDraw + int(element[2:])
        else:
            pass
        
    net_amount = deposit - withDraw
    return net_amount

trans_list = ["D:300", "D:200", "W:200", "D:100"]
print(calculate_net_amount(trans_list))