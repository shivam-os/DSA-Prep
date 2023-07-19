'''
Time complexity: O(M+N)
Space complexity: O(M+N)
Use 3 pointers:
First for items of first array, Second for items of second array & the third for position in third array
'''

def merge_sorted_arrays(arr1, arr2):
    res = [None] * (len(arr1) + len(arr2))
    p1 = 0
    p2 = 0
    p3 = 0

    #Place the items one by one while comparing them
    while (p1 < len(arr1) and p2 < len(arr2)):
        if arr1[p1] < arr2[p2]:
            res[p3] = arr1[p1]
            p1 += 1
        elif arr1[p1] > arr2[p2]:
            res[p3] = arr2[p2]
            p2 += 1
        else:
            res[p3] = arr1[p1]
            p3 += 1
            res[p3] = arr2[p2]
            p1 += 1
            p2 += 1

        p3 += 1
    
    #If arr1 is bigger and items are still left in it
    while (p1 < len(arr1)):
        res[p3] = arr1[p1]
        p1 += 1
        p3 += 1

    #If arr2 is bigger and items are still left in it
    while (p2 < len(arr2)):
        res[p3] = arr2[p2]
        p2 += 1
        p3 += 1

    return res

def array_input(arr): 
  size = int(input("Enter the size of array: "))
  for i in range(size):
      item = int(input("Enter the item: "))
      arr.append(item)

arr1 = []
array_input(arr1)
arr2 = []
array_input(arr2)
print(merge_sorted_arrays(arr1, arr2))

