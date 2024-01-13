inp = input("Enter space separated numbers in the list: ")
numbers = inp.split(" ")
numbers = [int(i) for i in numbers]
sum_numbers = sum(numbers)
print(sum_numbers)
