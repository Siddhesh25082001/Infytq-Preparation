#lex_auth_0127136251125350401190

def divisible_by_sum(number):
    
    #start writing your code here
    intNumber = number
    strNumber = str(number)
    sum = 0
    
    for digit in strNumber:
        sum = sum + int(digit)
        
    if intNumber % sum == 0: return True
    else: return False
        
number = 42
print(divisible_by_sum(number))