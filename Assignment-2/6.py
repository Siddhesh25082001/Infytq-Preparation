#lex_auth_012693810762121216155

def solve(heads, legs):
    error_msg = "No solution"
    chicken_count = 0
    rabbit_count = 0

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count
    if(legs % 2 == 0):
        chicken_count = int(( ( (4 * heads) - legs ) / 2 ))
        rabbit_count = int(((legs - (2 * heads)) / 2 ))
        
        if(chicken_count < 0 or rabbit_count < 0):
            print(error_msg)
        else:
            print(chicken_count, rabbit_count)
    else:
        print(error_msg)

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    # print(chicken_count, rabbit_count)
    # print(error_msg)

#Provide different values for heads and legs and test your program
solve(38, 131)