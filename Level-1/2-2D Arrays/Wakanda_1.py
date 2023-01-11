#Take input for the matrix
matRows = int(input())
matCols = int(input())
mat = []
for row in range(matRows):
  tempRow = []
  for cols in range(matCols):
    val = int(input())
    tempRow.append(val)
  mat.append(tempRow)

#Print elements in required pattern
for col in range(len(mat[0])):
  if (col % 2 == 0):
    for row in range(len(mat)):
      print(mat[row][col])
  else:
    for row in range(len(mat) - 1, -1, -1):
      print(mat[row][col])
