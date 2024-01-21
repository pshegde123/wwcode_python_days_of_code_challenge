
userInput = input("Enter a string: ")
inputList = list(userInput)
reverseList = inputList[::-1]
str_reversed = ''.join(reverseList)
print("Reversed string: ",str_reversed)