class Node:

    def __init__(self,data):
        self.data = data 
        self.next = None 

class LinkedList:

    def __init__(self):
        self.head = None 

    
    def addElement_Ending(self,data):

        new_Node = Node(data)

        if self.head is None:
            self.head = new_Node 
            return 

        temp = self.head 
        while temp.next is not None:
            temp = temp.next 
        
        temp.next= new_Node

    def find_maximum(self):

        maximum = 0
        temp = self.head 

        while temp:
            if temp.data[3] > maximum:
                maximum = temp.data[3] 
            
            temp = temp.next 
        
        return maximum

    def find_minimum(self):

        minimum = self.head.data[3]
        temp = self.head.next

        while temp:
            if temp.data[3] < minimum:
                minimum = temp.data[3]
            
            temp = temp.next 

        return minimum


    def print_all(self):

        temp = self.head 
        
        print("Printing Records", end='\n\n')
        while temp:
            print(temp.data)
            temp = temp.next 