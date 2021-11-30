#lex_auth_012693813706604544157

def find_max(num1, num2):
    max_num = -1
    
    l = []
    # Write your logic here
    if(num1 < num2):
        for i in range(num1, num2+1):
          if( ( (sum(list(map(int, str(i).strip())))) % 3 == 0 ) and ( len(str(i)) == 2 ) and (i % 5 == 0) ):
              l.append(i)
          else:
              continue
    else:
        max_num = -1
    
    if(len(l) == 0):
        max_num = -1
    else:
        max_num = max(l)
    
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num = find_max(10, 15)
print(max_num)