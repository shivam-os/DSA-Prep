def print_incr_decr(n):
    #Base condition
    if n == 0:
        return
    
    print(n)
    print_incr_decr(n - 1)
    print(n)

num = int(input("Enter a number: "))
print_incr_decr(num)
