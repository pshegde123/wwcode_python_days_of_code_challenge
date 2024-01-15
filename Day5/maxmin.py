inp = input("Enter space separated numbers in the list: ")
numbers = inp.split(" ")
numbers = [int(i) for i in numbers]
maxnum, minnum = max(numbers), min(numbers)
print(maxnum,minnum)
