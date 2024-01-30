user_input = input("Enter numbers separated by space: ")
nums = user_input.split(" ")
result_list = []
for i in nums:
    if int(i) % 2 == 0:
        result_list.append(int(i))
print(result_list)