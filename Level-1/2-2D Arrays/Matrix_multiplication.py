#Take input for first matrix
m1rows = int(input())
m1cols = int(input())
m1arr = []
for row in range(m1rows):
  m1temp = []
  for col in range(m1cols):
    val = int(input())
    m1temp.append(val)
  m1arr.append(m1temp)

#Taking input for second matrix
m2rows = int(input())
m2cols = int(input())
m2arr = []
for row in range(m2rows):
  m2temp = []
  for col in range(m2cols):
    val = int(input())
    m2temp.append(val)
  m2arr.append(m2temp)

#Multiply matrices
def matrixMultiplication(m1arr, m2arr):
  m3arr = []
  
  for row in range(len(m1arr)):
    m3temp = []
    for col in range(len(m2arr[0])):
      val = 0
      for comm in range(len(m2arr)):
        val += m1arr[row][comm] * m2arr[comm][col]
      m3temp.append(val)
    m3arr.append(m3temp)
    
  return m3arr;

#Check if matrices can even be multiplied
if (m1cols != m2rows):
  print("Invalid input")
else:
  m3arr = matrixMultiplication(m1arr, m2arr)
  for row in range(len(m3arr)):
    for col in range (len(m3arr[0])):
      print(m3arr[row][col], end=" ")
    print()
