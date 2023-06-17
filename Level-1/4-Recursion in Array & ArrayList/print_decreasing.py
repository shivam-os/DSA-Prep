def print_decreasing(n):
    #Base condition
    if n == 0:
        return
    
    print(n)
    print_decreasing(n - 1)

num = int(input("Enter the number: "))
print_decreasing(num)
