def power_logarithmic(num, times):
    #Time complexity: O(log(n))

    #Base condition
    if times == 0:
        return 1
    
    #If even number
    if times % 2 == 0:
        return power_logarithmic(num, times // 2) * power_logarithmic(num, times // 2)
    #If odd number
    else: 
        return power_logarithmic(num, times // 2) * power_logarithmic(num, times // 2) * num

num = int(input("Enter base: "))
power = int(input("Enter power: "))
print("Number raised to given power is:", power_logarithmic(num, power))
