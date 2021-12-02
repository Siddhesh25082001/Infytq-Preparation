def ans(s):
    
    stack = []
    for letter in s:
        if letter == '(' or letter == '[' or letter == '{':
            stack.append(letter)
        else:
            x = stack.pop()
            if letter == ')' and x != '(': return False
            elif letter == ']' and x != '[': return False
            elif letter == '}' and x != '{': return False
            else:
                continue
            
    if len(stack) == 0: return True
    else: return False

s = "[(])"
print(ans(s))