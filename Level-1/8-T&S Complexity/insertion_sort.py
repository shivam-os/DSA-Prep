def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j + 1] < arr [j]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

size = int(input("Enter the size of array: "))
arr = []

for i in range(size):
    item = int(input("Enter the item: "))
    arr.append(item)

print("Before sorting:", arr)
insertion_sort(arr)
print("After sorting:", arr)
