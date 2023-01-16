def solve(arr):
  #Create next greater element & assign -1 for last element
  nge = [None] * len(arr)
  nge[-1] = -1

  #Push the last array element to stack
  st = []
  st.append(arr[-1])

  #Traverse through array in reverse
  for i in range(len(arr) - 2, -1, -1):
    #Each element will perform: -, a, +
    while(len(st) > 0 and arr[i] >= st[-1]):
      st.pop()

    #If array is empty then, assign -1 otherwise nge is the top element
    if (len(st) == 0):
      nge[i] = -1
    else:
      nge[i] = st[-1]
      
    st.append(arr[i])

  return nge

#Main program
size = int(input())
arr = []

for i in range(size):
  value = int(input())
  arr.append(value)
  
ans = solve(arr)

for i in ans:
  print(i)
