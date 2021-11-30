#lex_auth_01269444890062848087

def find_correct(word_dict):
     
    #start writing your code here
    correct, almost, wrong = 0, 0, 0
    
    for key, value in word_dict.items():
        
        if key == value:
            correct = correct + 1
        
        else:
      
            if len(key) != len(value):
                wrong = wrong + 1
                continue
            incorrect = 0
            
            for i in range(min([len(key), len(value)])):
                if key[i] != value[i]:
                    incorrect = incorrect+1
                    if incorrect > 2:
                        wrong = wrong + 1
                        break

            if incorrect <= 2:
                almost = almost + 1

    return [correct, almost, wrong]

word_dict = {"THEIR": "THEIR", "BUSINESS":"BISINESS", "WINDOWS":"WINDMILL", "WERE":"WEAR", "SAMPLE":"SAMPLE"}
print(find_correct(word_dict))