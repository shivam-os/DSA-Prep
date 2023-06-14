#Take input for array
def array_input(arr):
    n = int(input("Enter the size of array: "))
    for i in range(n):
        element = int(input("Enter the element: "))
        arr.append(element)

#Take input for array 1
a1 = []
array_input(a1)

#Take input for array 2
a2 = []
array_input(a2)

#Create dictionary using a1 values
a1_elements = {}
for i in a1:
    if i in a1_elements:
        a1_elements[i] += 1
    else:
        a1_elements[i] = 1

#Print the found values of a2 from a1
for i in a2:
    if i in a1_elements:
        print(i)
        del a1_elements[i]

