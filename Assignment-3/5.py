#lex_auth_012693816331657216161

def encode(message):
    
    #Remove pass and write your logic here
    count = 1
    formatMessage = message + "0"
    encodedMessage = []
    
    for letter in range(0, len(message)):
        if(formatMessage[letter] == formatMessage[letter + 1]):
            count = count + 1
        else:
            encodedMessage.append(str(count))
            encodedMessage.append(formatMessage[letter])
            count = 1
    
    return ("".join(encodedMessage))

#Provide different values for message and test your program
encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)