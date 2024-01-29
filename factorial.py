num = int(input("Enter a number: "))

def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num*factorial(num-1)

print("Factorial of "+str(num)+" = "+str(factorial(num)))