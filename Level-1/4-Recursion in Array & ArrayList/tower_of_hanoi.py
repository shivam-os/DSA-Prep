def toh(disks, towerA, towerB, towerC):
    #Base condition
    if disks == 0:
        return

    #Print instructions to move disks from tower A to tower C with help of B
    toh(disks - 1, towerA, towerC, towerB)

    #Print instruction to move disk from tower A to tower B
    print(disks, "[", towerA, "->", towerB, "]")

    #Print instructions to move disks from tower C to tower B with help of A
    toh(disks - 1, towerC, towerB, towerA)
    
disks = int(input("Enter the number of disks: "))
tower1 = input("Enter id of tower 1: ")
tower2 = input("Enter id of tower 2: ")
tower3 = input("Enter id of tower 3: ")
toh(disks, tower1, tower2, tower3)
