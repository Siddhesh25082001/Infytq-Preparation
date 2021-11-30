#lex_auth_0127135857243832321154

def seed_no(number, ref_no):
    
    #start writing your code here
    intNumber = number
    strNumber = str(number)
    
    for digit in strNumber:
        intNumber = intNumber * int(digit)
        
    if intNumber == ref_no: return True
    else: return False
    
number = 45
ref_no = 1000
print(seed_no(number, ref_no))