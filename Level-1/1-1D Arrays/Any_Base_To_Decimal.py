def convertToDecimal(number, base):
    convertedNumber = 0
    power = 0

    while number > 0:
        remainder = number % 10
        convertedNumber += remainder * (base**power)
        number = number // 10
        power += 1

    return convertedNumber


number = int(input("Enter the number to convert: "))
base = int(input("Enter the base of the number: "))
print("Number in decimal form is:", convertToDecimal(number, base))
