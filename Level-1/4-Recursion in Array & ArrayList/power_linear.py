def power_linear(num, times):
    #Base condition
    if times == 0:
        return 1
    
    return num * power_linear(num, times - 1)

num = int(input("Enter base: "))
power = int(input("Enter power: "))
print("Number raised to given power is:", power_linear(num, power))
