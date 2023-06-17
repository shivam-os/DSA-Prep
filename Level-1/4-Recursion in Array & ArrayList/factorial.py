def factorial(n):
    #Base condition
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial of given number:", factorial(num))
