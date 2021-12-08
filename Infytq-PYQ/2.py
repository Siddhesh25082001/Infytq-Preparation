def solve2(sentence2):
    newSentence = ""
    for letter in sentence2:
        if letter not in newSentence:
            newSentence += letter
            
    return newSentence[::-1]

sentence2 = "infosys"
print(solve2(sentence2))