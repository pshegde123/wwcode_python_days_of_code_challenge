names = input("Enter space separated list entries :").split(" ")
print(names)
result = list(set(names))
# for item in names:    
#     if item not in result:
#         result.append(item)
print("List after removing duplicates = ",result)