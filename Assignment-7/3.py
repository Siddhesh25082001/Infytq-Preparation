#lex_auth_01269446533799116898

def check_perfect_number(number):
    
    #start writing your code here
    factors = []
    for i in range(1, (number + 1)):
        if(number % i == 0):
            factors.append(i)
    
    s = sum(factors[0:-1])
    if s == number: return True
    else: return False

def check_perfectno_from_list(no_list):
    
    #start writing your code here
    l = []
    for num in no_list:
        if num > 5:
            f = check_perfect_number(num)
            if f == True: l.append(num)
        else:
            continue

    return l

perfectno_list = check_perfectno_from_list([87, 76, 567, 99, 0])
print(perfectno_list)