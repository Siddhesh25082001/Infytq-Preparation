#lex_auth_0127135773590405121141

def bracket_pattern(input_str):
    
    #Remove pass and write your code here
	countOpen, countClose = 0, 0
	for ch in input_str:
	    if ch == '(':
	        countClose = countClose + 1
	    else:
	        countOpen = countOpen + 1
	
	if (countOpen != countClose): return False
	elif ( input_str[0:1] == ')' or input_str[-1:] == '(' ): return False
	else: return True

input_str = "(())("
print(bracket_pattern(input_str))