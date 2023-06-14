def matrix_input(mat):
    row = int(input("Enter the row size:"))
    col = int(input("Enter the col size: "))

    for i in range(row):
        temp = []
        for j in range(col):
            item = int(input("Enter the item: "))
            temp.append(item)
        mat.append(temp)

def wakanda_path(mat):
    row = len(mat)
    col = len(mat[0])

    for j in range(col):
        if j % 2 == 0:
            for i in range(row):
                print(mat[i][j])
        else:
            for i in range(row - 1 , 0, -1):
                print(mat[i][j])
                
#Create matrix
mat = []
matrix_input(mat)
wakanda_path(mat)
