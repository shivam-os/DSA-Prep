def convertToBase(decimal, base):
    power = 0
    convertedNumber = 0

    while decimal > 0:
        remainder = decimal % base
        convertedNumber += remainder * (10**power)
        decimal = decimal // base
        power += 1

    return convertedNumber


decimal = int(input("Enter the decimal number: "))
base = int(input("Enter the base: "))
print("Converted number in given base:", convertToBase(decimal, base))
