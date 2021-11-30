#lex_auth_0127136011356405761166

def generate_sentences(subjects, verbs, objects):
	
	#start writing your code here
	sentence = ""
	sentence_list = []
	
	for s in subjects:
	    for v in verbs:
	        for o in objects:
	            sentence = s + " " + v + " " + o
	            sentence_list.append(sentence)
	
	return sentence_list

subjects = ["I", "You"]
verbs = ["love", "play"]
objects = ["Hockey", "Football"]
print(generate_sentences(subjects,verbs,objects))