#lex_auth_0127135869481369601150

def list123(nums):
    
    #start writing your code here
    flag = False
    
    for num in range(0, len(nums) - 2):
        if nums[num] == 1 and nums[num + 1] == 2 and nums[num + 2] == 3:
            flag = True
            return True
        else:
            continue
    
    if not flag: return False
    
nums = [1, 2, 3, 4, 5]
print(list123(nums))