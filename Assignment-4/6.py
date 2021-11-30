#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word = ""
    frequency = 0
    
    count = dict()
    data = data.lower()
    words = data.split()
    
    for word in words:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1
    
    values = count.values()
    frequency = max(values)
    
    s = ""
    for key, value in count.items():
        if value == frequency and len(key) > len(s):
            word = key
            s = word
        else:
            continue
    
    print(word, frequency)

#Provide different values for data and test your program.
data = "the task b b a a"
max_frequency_word_counter(data)