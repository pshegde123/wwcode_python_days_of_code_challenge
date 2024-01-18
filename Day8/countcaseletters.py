def countCharacters(inputs):
    lowercaseCount = 0
    uppercaseCount = 0
    for letter in inputs:        
        if letter.islower():
            lowercaseCount +=1
        elif letter.isupper():
            uppercaseCount +=1
    print("Upper case letter count:",uppercaseCount)
    print("Lower case letter count:",lowercaseCount)


inputs = input("Enter a string: ")
countCharacters(inputs)