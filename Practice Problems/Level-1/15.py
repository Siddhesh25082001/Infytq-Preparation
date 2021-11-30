#lex_auth_0127136213490565121191

def hcf(a, b):
    
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)

def find_gcd(num1, num2):
    
    #start writing your code here
    gcd = hcf(num1, num2)
    return gcd

num1 = 45
num2 = 9
print(find_gcd(num1, num2))