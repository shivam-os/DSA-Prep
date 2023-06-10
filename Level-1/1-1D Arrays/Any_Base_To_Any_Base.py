def convertToDecimal(number, base):
    convertedNumber = 0
    power = 0

    while (number > 0):
        remainder = number % 10
        convertedNumber += remainder * (base ** power)
        number = number // 10
        power += 1
    
    return convertedNumber

def decimalToBase(decimal, base):
    convertedNumber = 0
    power = 0

    while (decimal > 0):
        remainder = decimal % base
        convertedNumber += remainder * (10 ** power)
        decimal = decimal // base
        power += 1
    
    return convertedNumber

number = int(input("Enter the number: "))
base1 = int(input("Enter the base of the given number: "))
base2 = int(input("Enter the base to convert in: "))

#First convert the given number in decimal form
decimal = convertToDecimal(number, base1)

#Now convert the given decimal number to required base number
newNumber = decimalToBase(decimal, base2)

print("Given number with changed base:", newNumber)
