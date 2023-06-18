def selection_sort(arr):
  for i in range(len(arr) - 1):
    min = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min]:
        min = j
    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp

size = int(input("Enter the size of array: "))
arr = []

for i in range(size):
    item = int(input("Enter the item: "))
    arr.append(item)

print("Before sorting:", arr)
selection_sort(arr)
print("After sorting:", arr)
                 
