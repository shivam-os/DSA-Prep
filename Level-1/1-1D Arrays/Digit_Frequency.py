def findDigitCount(number, digit):
    count = 0
    for i in number:
        if i == digit:
            count += 1
    return count

number = input("Enter the number: ")
digit = input("Enter the digit to find: ")

print("Digit's number of appearances:", findDigitCount(number, digit))
