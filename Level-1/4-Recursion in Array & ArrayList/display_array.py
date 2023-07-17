def print_array(arr, idx):
    #Base condition
    if idx == len(arr):
        return
    
    print(arr[idx])
    print_array(arr, idx + 1)

def print_reverse(arr, idx):
    #Base condition
    if idx == len(arr):
        return
    
    print_reverse(arr, idx + 1)
    print(arr[idx])

size = int(input("Enter the size of array: "))
arr = []
for i in range(size):
    item = int(input("Enter the element: "))
    arr.append(item)

print("Array: ")
print_array(arr, 0)
print("Array in reverse: ")
print_reverse(arr, 0)

