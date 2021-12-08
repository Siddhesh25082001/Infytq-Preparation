def solve1(sentence1):
    numList = sentence1.split(",")
    num1, num2 = 0, 0
    
    lower = numList.index("4")
    upper = numList.index("7")
    
    num1 = (numList[:lower] + numList[upper + 1:])
    num1 = sum(list(map(int, num1)))
    num2 = int("".join(numList[lower:upper + 1]))
    
    return num1 + num2

sentence1 = "3,1,6,4,2,3,7,2"
print(solve1(sentence1))