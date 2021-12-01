#lex_auth_012694465248329728100

def validate_name(name):
    
    #Start writing your code here
    if name == "" or len(name) > 15 or name.isalpha() == False: return False
    else: return True

def validate_phone_no(phno):
    
    #Start writing your code here
    specialCharacters = "!@#$%^&*()-+?_=,<>/"
    if len(phno) != 10 or any(ch in specialCharacters for ch in phno) == True or len(set(phno)) == 1: return False
    else: return True

def validate_email_id(email_id):
    
    #Start writing your code here
    domainName = ['gmail', 'yahoo', 'hotmail']
    flag = False
    
    for email in email_id:
        if "gmail" in email_id or "yahoo" in email_id or "hotmail" in email_id: flag = True
        else: flag = False
        
    if email_id.count('@') > 1 or email_id.count('.com') > 1 or email_id[-4:] != ".com" or flag == False: return False
    else: return True

def validate_all(name, phone_no, email_id):

    #Start writing your code here
    if validate_name(name) and validate_phone_no(phone_no) and validate_email_id(email_id):
        print("All the details are valid")
    elif not validate_name(name): print("Invalid Name")
    elif not validate_phone_no(phone_no): print("Invalid phone number")
    elif not validate_email_id(email_id): print("Invalid email id")
    else: pass

    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    #print("Invalid Name")
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")

#Provide different values for name, phone_no and email_id and test your program
# validate_all("Tina", "9994599998", "tina@yahoo.com")