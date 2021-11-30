#lex_auth_012693825794351104168

def ignoreSpace(msg):
    newMsg = msg.replace(" ", "")
    return newMsg

def find_common_characters(msg1, msg2):
    
    #Remove pass and write your logic here
    formatMsg1 = ignoreSpace(msg1)
    formatMsg2 = ignoreSpace(msg2)
    
    finalMessage = []
    for letter in formatMsg1:
        if letter in formatMsg2 and letter not in finalMessage:
            finalMessage.append(letter)
    
    if len(finalMessage) == 0:
        return -1
    else:
        return "".join(finalMessage)

#Provide different values for msg1,msg2 and test your program
msg1 = "I like Python"
msg2 = "Java is a very popular language"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)