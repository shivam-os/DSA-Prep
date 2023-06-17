def print_increasing(n):
    #Base condition
    if n == 0:
        return

    print_increasing(n - 1)
    print(n)

num = int(input("Enter the number: "))
print_increasing(num)
