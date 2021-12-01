#lex_auth_01269443477535129681

def find_duplicates(list_of_numbers):
    
    #start writing your code here
    count = dict()
    for num in list_of_numbers:
        if num in count:
            count[num] = count[num] + 1
        else:
            count[num] = 1

    duplicate = []
    for key, value in count.items():
        if value >= 2:
            duplicate.append(key)
        else:
            continue
        
    return duplicate

list_of_numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
list_of_duplicates = find_duplicates(list_of_numbers)
print(list_of_duplicates)