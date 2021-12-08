#lex_auth_0127136008767324161169

def close_number(num1, num2, num3):
    
    #start writing your code here
    helperList = []
    helperList.append(num1 - num2)
    helperList.append(num1 - num3)
    helperList.append(num2 - num1)
    helperList.append(num2 - num3)
    helperList.append(num3 - num1)
    helperList.append(num3 - num2)

    count = 0
    for num in helperList:
        if abs(num) == 1 or num == 0:
            count = count + 1
            
    if count == 2: return True
    else: return False
    
print(close_number(5, 4, 2))