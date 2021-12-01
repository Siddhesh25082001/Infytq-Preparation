#lex_auth_01269442114344550475

def checkPallindrome(word, start, end):
    
    if start == end :
        return True
    
    elif len(word) == 2:
        if word[0] == word[1]: return True
        else: return False
        
    else: 
        if word[start] == word[end]:
            return checkPallindrome(word, start + 1, end - 1)
        else:
            return False
    
def is_palindrome(word):
    
    #Remove pass and write your logic here
    word = word.lower()
    start = 0
    end = len(word) - 1
    
    if checkPallindrome(word, start, end): return True
    else: return False

#Provide different values for word and test your program
result = is_palindrome("mm")

if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")