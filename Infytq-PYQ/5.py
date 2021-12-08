def solve5(sentence5):
    stack = []
    
    for i in range(0, len(sentence5)):
        if sentence5[i] == '(' or sentence5[i] == '[' or sentence5[i] == '{':
            stack.append(sentence5[i])
        else:
            if len(stack) == 0: return i + 1
            else:
                x = stack.pop()
                if sentence5[i] == ')' and x == '(': continue
                elif sentence5[i] == ']' and x == '[': continue
                elif sentence5[i] == '}' and x == '{': continue
                else: return i + 1

    return 0

sentence5 = "{([])][]"
print(solve5(sentence5))