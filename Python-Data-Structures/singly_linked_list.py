#Linked list implementation in Python

#For creating individual nodes with 2 data fields- data: representing the value, next: address/reference of next node
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

#For creating linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    #Insert the data at beginning of linked list
    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    #Traverse the entire linked list
    def traverse(self):
        temp = self.head
        result = ""

        while(temp != None):
            result += str(temp.data) + "->"
            temp = temp.next

        print(result[:-2])

    #Insert the data at end of the linked list
    def insert_at_tail(self, value):
        #If linked list is empty
        if self.head == None:
            self.insert_at_head(value)
        else:
            new_node = Node(value)
            temp = self.head

            while(temp.next != None):
                temp = temp.next

            temp.next = new_node
            self.count += 1

    #Insert the data after an already existing linked list value
    def insert_after_value(self, after, value):
        new_node = Node(value)
        temp = self.head

        while(temp != None):
            if temp.data == after:
                new_node.next = temp.next
                temp.next = new_node
                self.count += 1
                return

            temp = temp.next

        return print("Invalid value!")

    #Delete item at head of linked list
    def delete_at_head(self):
        if self.head == None:
            print("Linked list is empty!")
        else:
            self.head = self.head.next

    #Delete item at tail of linked list
    def delete_at_tail(self):
        if self.head == None:
            print("Linked list is empty!")
        else:
            temp = self.head

            while(temp.next.next != None):
                temp = temp.next

            temp.next = None

    #Delete a certain value from linked list
    def delete_value(self, value):
        temp = self.head

        while (temp != None):
            if temp.next.data == value:
                temp.next = temp.next.next
                return print("Deleted!")

            temp = temp.next

        return print("Invalid value")

    #Delete the entire linked list
    def empty(self):
        self.head = None

    #Return the index of given value in linked list
    def search_value(self, value):
        temp = self.head
        index = 0

        while (temp != None):
            if temp.data == value:
                return print(index)
                
            temp = temp.next
            index += 1

        return print("Invalid value!")

    #Return the item present at given index (starts from 0)
    def item_at_index(self, index):
        temp = self.head
        curr = 0

        while (temp != None):
            if index == curr:
                return print(temp.data)
            
            temp = temp.next
            curr += 1

        return print("Invalid index!")
