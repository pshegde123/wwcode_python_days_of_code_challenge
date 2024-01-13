vowel_count = 0
vowels = ['a','e','i','o','u']
input_str = input("Enter a string: ")
for ch in input_str:
    if ch.lower() in vowels:
        vowel_count+=1
print("Number of vowels in the string:  ",vowel_count)