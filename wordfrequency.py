sentence = input("Enter a sentence: ")
modified_sentence = sentence.split(" ")
word_set = set(modified_sentence)
print(word_set)
for word in word_set:
    print("Count of "+word+" = "+str(modified_sentence.count(word)))