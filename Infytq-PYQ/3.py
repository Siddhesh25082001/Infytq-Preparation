def solve3(otp):
    odd = []
    otp = str(otp)
    
    for i in range(1, len(otp), 2):
        odd.append(int(otp[i]) * int(otp[i]))
        
    ans = "".join(list(map(str, odd)))
    return ans[:4]

otp = 5624381275
print(solve3(otp))