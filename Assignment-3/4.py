#lex_auth_012693819159732224162

def check_palindrome(word):
    return True if word == word[::-1] else False

status = check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")