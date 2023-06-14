def create_matrix(mat):
    row = int(input("Enter the row size: "))
    col = int(input("Enter the column size: "))
    
    for i in range(row):
        temp = []
        for j in range(col):
            item = int(input("Enter the item: "))
            temp.append(item)
        mat.append(temp)

def print_matrix(mat):
    print("Matrix: ")

    # for i in range(len(mat)):
    #     for j in range(len(mat[0])):
    #         print(mat[i][j], " ", end="")
    #     print()

    #Python way
    for i in mat:
        for j in i:
            print(j, " ", end="")
        print()


def multiply_matrix(matA, matB):
    if len(matA[0]) != len(matB):
        return "Invalid input"
    
    matC = []
    row = len(matA)
    col = len(matB[0])
    comm = len(matA[0])

    for i in range(row):
        temp = []
        for j in range(col):
            item = 0
            for k in range(comm):
                item += matA[i][k] * matB[k][j]
            temp.append(item)
        matC.append(temp)

    print_matrix(matC)

#Create first matrix
matA = []
create_matrix(matA)
print_matrix(matA)

#Create second matrix
matB = []
create_matrix(matB)
print_matrix(matB)

#Multiply the first & second matrix
multiply_matrix(matA, matB)


