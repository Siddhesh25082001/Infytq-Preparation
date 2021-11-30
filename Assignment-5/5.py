#lex_auth_01269438947391897654

#Global variable
list_of_marks = (12, 18, 25, 24, 2, 5, 18, 20, 20, 21)

def find_more_than_average():
    average = sum(list_of_marks) / len(list_of_marks)

    count = 0
    for marks in list_of_marks:
        if(marks > average):
            count = count + 1
        else:
            continue
        
    return  ( count / len(list_of_marks) ) * 100

def generate_frequency():
    count = dict()
    for num in list_of_marks:
        if num in count:
            count[num] = count[num] + 1
        else:
            count[num] = 1
        
    frequency = []
    
    for num in range(0, 26):
        if num in count.keys():
            frequency.append(count[num])
        else:
            frequency.append(0)
            
    return frequency       
                
def sort_marks():
    l = list(list_of_marks)
    l.sort()
    return l

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())