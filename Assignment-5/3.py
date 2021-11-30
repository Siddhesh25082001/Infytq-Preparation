#lex_auth_01269441810970214471

def check_double(number):
    
    #Remove pass and write your logic here
    twice = 2 * number
    number = str(number)
    twice = str(twice)
    
    for digit in number:
        if digit not in twice:
            return False
        else:
            continue
        
    return True

#Provide different values for number and test your program
print(check_double(125874))