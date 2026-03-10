# Task 1: Calculate Factorial Using a Function 

#taking the number by using input module
num = int(input("Enter a number: "))

#defined with factorial name and it takes ' n ' number and calculates the factorial using recursion
def factorial(n):  
    # if n == 1 or n == 0 then it returns the 1 value otherwise it goes to else part
    if n == 0 or n == 1:
        return 1
    else:
        #if 'n' > 1 then it subtracts with 1 and multiply with 'n' number  and stores result in fact variable
        fact = n * factorial(n - 1) 
        # it returns the factorial value
        return fact 
#calling function by variable and returning value from function
result = factorial(num) 
print(f"factorial of {num} is {result}") 