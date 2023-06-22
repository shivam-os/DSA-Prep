def print_zigzag(num):
    if num == 1:
        return "1 1 1 "
    
    result = print_zigzag(num - 1)
    snum = str(num) + " "

    return snum + result + snum + result + snum

def print_zigzag_2(num):
    if num == 0:
        return
    
    print(num, end=" ")
    print_zigzag_2(num - 1)
    print(num, end=" ")
    print_zigzag_2(num - 1)
    print(num, end=" ")
  
num = int(input("Enter a number: "))
print(print_zigzag_2(num))
