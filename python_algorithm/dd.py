class Node:
    
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
    
    def test(self):
        curr=self.head.next
        data=curr.data
        print (data)

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head.next

        while curr.data!=None and x < curr.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head

        while curr.next.data!=None and x < curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def __repr__(self):
        if self.nodeCount==0:
            return 'DoubleLinkedList is empty'
        s = ''
        curr = self.head.next
        while curr.next is not None:
            s += repr(curr.data)
            if curr.next is not self.tail:
                s += ' -> '
            curr = curr.next
        return s


    def getLength(self):
        size=0
        curr= self.head.next
        while curr is not None:
            size+=1
            curr=curr.next
        size-=1
        return(size)

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr=prev.next
        after=curr.next
        prev.next=after
        after.prev=prev
        data=curr.data
        self.nodeCount-=1
        del curr
        return data


    def popBefore(self, next):
        curr=next.prev
        prev=curr.prev
        prev.next=next
        next.prev=prev
        data=curr.data
        self.nodeCount-=1
        del curr
        return data


    def popAt(self, pos):
        if pos<1 or pos>self.nodeCount:
            raise IndexError
        if pos>(self.nodeCount//2):
            if pos==self.nodeCount:
                next=self.tail
            else:
                next=self.getAt(pos+1)
            return self.popBefore(next)
        if pos<=(self.nodeCount//2):
            if pos==1:
                prev=self.head
            else:
                prev=self.getAt(pos-1)
            return self.popAfter(prev)

	
    def concat(self, L):
        self.tail.prev.next=L.head.next
        L.head.next.prev=self.tail.prev
        self.tail=L.tail
        self.nodeCount+=L.nodeCount

L=DoublyLinkedList()
a=Node("폴")
b=Node("라")
c=Node("민")
d=Node("알")
f=Node("고")
g=Node("리")
h=Node("즘")

L.insertAt(1,a)
L.insertAt(2,b)
L.insertAt(3,c)
L.insertAt(4,d)
L.insertAt(5,f)
L.insertAt(6,g)
L.insertAt(7,h)

print(L)
print(L.getLength())
L.test()
curr=L.head.next
print(curr.data)