# Input: Program to reverse a string after removing duplicates

# Test Case 1: infosys  ->  Output: ysofni
# Test Case 2: google   ->  Output: elog

def solve2(sentence):
    
    unique = ""
    for letter in sentence:
        if letter not in unique:
            unique = unique + letter
            
    print(unique[::-1])

sentence = "google"
solve2(sentence)