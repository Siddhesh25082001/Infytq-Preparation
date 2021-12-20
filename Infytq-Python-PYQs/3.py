# Input: 
# Input will be a number
# You have to return a 4 digit OTP by squaring the digits at odd places and return the first 4 digits

# Test Case 1: 5624381275
# Digits at Odd places: 6, 4, 8, 2, 5
# Squaring of these Digits: 36, 16, 64, 4, 25
# Returning 3616

def solve3(num):
    
    strNumber = str(num)
    numList = list(strNumber)               # numList = ["5", "6", "2", ... "5"]
    
    ans = []
    for i in range(1, len(numList), 2):
        ans.append(int(numList[i]))         # ans = [6, 4, 8, 2, 5]
        
    for i in range(0, len(ans)):
        ans[i] = ans[i] * ans[i]            # ans = [36, 16, 64, 4, 25]
        
    final = list(map(str, ans))             # final = ["36", "16", "64", "4", "25"]
    print("".join(final)[:4])               # 3616
        
num = 5624381275
solve3(num)