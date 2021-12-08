#lex_auth_0127136426924195841210

def check_well_formatted(input_item, list_label):
    
    #Start writing your code here
    if type(input_item) == list:
        if len(input_item) >= 2:
            if input_item[0] in list_label:
                for i in input_item[1:]:
                    if type(i) == str or check_well_formatted(i, list_label):
                        continue
                    else: return False
                return True
            else: return False
        else: return False
    else: return False


input_list1 = ['VP', ['V', 'eat']]
list_label1 = ['VP', 'V']
result = check_well_formatted(input_list1, list_label1)
if result is True:
    print("Well formatted")
else:
    print("Not Well formatted")