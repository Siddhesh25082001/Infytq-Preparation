# Input: 
# A string of comma separated numbers are given such that the numbers 4 and 7 are already present int the list
# Assume that 7 always comes after 4 in the given string

# Case-1: num1 = add all numbers which do not lie between 4 and 7 in input (excluding 4 and 7)
# Case-2: num2 = numbers formed by concatenation of all numbers from 4 to 7 (including 4 and 7)

# Output: num1 + num2

def solve1(sentence):
    
    numList = sentence.split(",")
    
    lower = numList.index("4")
    upper = numList.index("7")
    
    num1, num2 = 0, 0
    
    num1 = numList[0:lower] + numList[upper+1:]     # num1 = [ "3", "1", "6", "2" ]
    num1 = sum(list(map(int, num1)))                # num1 = 12
    
    num2 = int("".join(numList[lower:upper+1])      # num2 = 4237
    
    print(num1 + num2)
   
   
sentence1 = "3,1,6,4,2,3,7,2" 
solve1(sentence1)