#lex_auth_0127135739583692801137

def add_string(str1):
    
  #start writing your code here
    if (str1[-3:] == "ing"):
        str1 = str1 + "ly"
    elif (len(str1) < 3):
        pass
    else:
        str1 = str1 + "ing"

    return str1

str1 = "amazing"
print(add_string(str1))