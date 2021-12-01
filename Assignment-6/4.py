#lex_auth_01269442760027340879

def findFactors(number):
    
    factors = []
    
    for i in range(1, (number + 1) ):
        if(number % i == 0):
            factors.append(i)
    
    return factors

def find_smallest_number(num):
    
    #start writing your code here
    i = 1
    countFactors = 0
    
    while(True):
        
        countFactors = findFactors(i)
        
        if len(countFactors) == num:
            break
        
        else:
            i = i + 1
            
    return countFactors[-1]
        
num = 16
print("The number of divisors : ", num)
result = find_smallest_number(num)
print("The smallest number having",num," divisors: ", result)