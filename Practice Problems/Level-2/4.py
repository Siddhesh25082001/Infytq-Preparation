#lex_auth_0127136357122129921205

def check_squares(number):
    
    #start writing your code here
    for i in range(0, number):
        for j in range(0, number):
            if i**2 + j**2 == number:
                return True
    
    return False

number = 68
print(check_squares(number))