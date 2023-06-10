def addBaseNumbers(num1, num2, base):
    sum = 0
    carry = 0
    power = 0

    while num1 > 0 or num2 > 0 or carry > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10
        digitSum = digit1 + digit2 + carry

        thirdDigit = digitSum % base
        carry = digitSum // base
        sum += thirdDigit * (10 ** power)

        num1 //= 10
        num2 //= 10
        power += 1

    return sum


base = int(input("Enter the base: "))
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Addition:", addBaseNumbers(num1, num2, base))
