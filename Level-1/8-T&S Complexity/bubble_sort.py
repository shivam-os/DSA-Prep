'''
Intiuition: Bubble up the largest element to end of array.
'''
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr [j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

size = int(input("Enter the size of array: "))
arr = []

for i in range(size):
    item = int(input("Enter the item: "))
    arr.append(item)

print("Before sorting:", arr)
bubble_sort(arr)
print("After sorting:", arr)
