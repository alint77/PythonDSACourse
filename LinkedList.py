class Node :
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self,value) :
        newNode=Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
    
    def append(self,value):
        newNode = Node(value)
        currNode = self.tail
        currNode.next = newNode
        self.tail=newNode
        self.length +=1
    
    def insert(self,index,value):
        if(index>self.length or index<0):
            raise IndexError
            
        newNode = Node(value)

        if(index==self.length):
            currNode=self.tail
            currNode.next=newNode
            self.tail=newNode
            self.length+=1
            return
        
        if(index==0):
            self.prepend(value)
            return
        
        currNode=self.head
        for i in range(index):
            currNode=currNode.next
        newNode.next=currNode.next
        currNode.next=newNode
        self.length+=1

    def prepend(self,value):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode
        self.length += 1

    def getValue(self,index):
        if(index < 0 or index>=self.length):
            raise IndexError
        
        currNode=self.head
        for i in range(index):
            currNode=currNode.next
        
        return currNode.value
    
    def getNode(self,index):
        if(index < 0 or index >= self.length):
            raise IndexError
        currNode=self.head
        for i in range(index):
            currNode=currNode.next
        return currNode
        
    
    def delete(self,index):

        if(index < 0 or index >= self.length):
            raise IndexError
        if(index == self.length - 1):
            self.pop()
            return
        if(index==0):
            self.head=self.head.next
            self.length-=1
            return
        currNode=self.head

        for i in range(index - 1):
            currNode=currNode.next
        
        currNode.next = currNode.next.next
        self.length-=1

    def pop(self):
        if(self.length == 0):
            raise IndexError
        if(self.length == 1):
            tempValue = self.head.value
            self.head = self.tail = None
            self.length -= 1
            return tempValue
            
        currNode=self.head
        while(currNode.next != self.tail):
            currNode=currNode.next
        tempValue= self.tail.value
        self.tail=currNode
        self.tail.next=None
        self.length-=1
        return tempValue
    
    def updateValue(self,index,value):
        if(index < 0 or index>=self.length):
            raise IndexError
        
        currNode=self.head
        for i in range(index):
            currNode=currNode.next
        
        currNode.value = value

    
    def reverse(self):
        if self.length <=1:
            return     
        currNode = self.head
        prevNode = None
        self.tail=self.head
        for i in range (self.length):
            tempNext = currNode.next
            currNode.next = prevNode
            prevNode=currNode
            currNode=tempNext
        self.head = prevNode
        
 
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.insert(1,0.5)
my_linked_list.insert(0,-1)
my_linked_list.insert(6,4)
my_linked_list.updateValue(2,0.1)


for i in range(my_linked_list.length):
    print(my_linked_list.getValue(i))

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

my_linked_list.reverse()

for i in range(my_linked_list.length):
    print(my_linked_list.getValue(i))


print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    