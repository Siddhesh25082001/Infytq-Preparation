#lex_auth_0127135945621340161163

def string_both_ends(input_string):
    
	#start writing your code here
	newString = ""
	if len(input_string) < 2: return -1
	elif len(input_string) == 2:
	    newString = input_string[0:2] + input_string[0:2]
	else:
	    newString = input_string[0:2] + input_string[-2:]
	    
	return newString    
	    
input_string = "w3w"
print(string_both_ends(input_string))