def fibonacci_numbers(num): 
    if num == 0: 
        return 0
    elif num == 1: 
        return 1
    else:         
        return fibonacci_numbers(num-2)+fibonacci_numbers(num-1) 
  
  
limit = int(input("Enter a number upto which you wish to see fibonacci series:"))
for i in range(0, limit): 
    print(fibonacci_numbers(i), end=" ") 