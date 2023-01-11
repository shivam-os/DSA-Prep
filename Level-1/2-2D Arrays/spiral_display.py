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

#Print elements in spiral pattern
minr = 0
maxr = len(mat) - 1
minc = 0
maxc = len(mat[0]) - 1
size = len(mat) * len(mat[0])
ctr = 0

while (ctr < size):
  #Print left wall
  i = minr
  j = minc
  while (i <= maxr and ctr < size):
    print(mat[i][j])
    i += 1
    ctr += 1
  minc += 1

  #Print bottom wall
  i = maxr
  j = minc
  while (j <= maxc and ctr < size):
    print(mat[i][j])
    j += 1
    ctr += 1
  maxr -= 1

  #Print right wall
  i = maxr
  j = maxc
  while (i >= minr and ctr < size):
    print(mat[i][j])
    i -= 1
    ctr += 1
  maxc -= 1

  #Print top wall
  i = minr
  j = maxc
  while (j >= minc and ctr < size):
    print(mat[i][j])
    j -= 1
    ctr += 1
  minr += 1
