#lex_auth_01269445968039936095

def digitSum(number):
    n = str(number)
    list_of_number = list(map(int, n.strip()))
    return sum(list_of_number)

def validate_credit_card_number(card_number):
    
    #start writing your code here
    card = str(card_number)
    reverseCard =  card[::-1]
    
    a = []
    for i in range(1, len(reverseCard), 2):
        a.append(2 * int(reverseCard[i]))
        
    for i in range(0, len(a)):
        if a[i] > 9:
            a[i] = digitSum(a[i])
        else:
            continue
        
    s = sum(a)
    add = 0
    for i in range(0, len(reverseCard), 2):
        add = add + int(reverseCard[i]) 
        
    if (s + add) % 10 == 0: return True
    else: return False
    
card_number = 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result = validate_credit_card_number(card_number)

if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")