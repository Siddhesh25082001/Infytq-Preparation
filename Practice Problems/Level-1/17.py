#lex_auth_0127136253311385601197

def check_occurence(string):
    
    #start writing your code here
    mat, jet = 0, 0
    string = string.lower()
    words = string.split(" ")
    
    for word in words:
        if word == "mat": mat = mat + 1
        elif word == "jet": jet = jet + 1
        else: continue
    
    if mat == jet: return True
    else: return False
        
string = "mat jet Jet Mat"
print(check_occurence(string))