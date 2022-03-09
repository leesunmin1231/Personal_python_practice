class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s
    
    # 연결 리스트에 특정 요소를 찾는 메소드 -> 특정 원소 참조
    # 몇번째 있는 노드를 찾을 것인지 위치를 입력 받고
    # pos 번째에 있는 노드 전체를 리턴한다.
    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head # 초기 node 위치 저장
        while i < pos:
            curr = curr.next # 다음 node 위치 저장
            i += 1
        return curr

    # 연습 문제 연결리스트 순회
    def traverse(self):
        lst=[]
        if self.nodeCount==0:
            return []
        else:
            curr = self.head
            i=1
            while i<=self.nodeCount:
                lst.append(curr.data)
                curr = curr.next
                i+=1
            return lst

    # 연결 리스트 길이 알기
    def getLength(self):
        return self.nodeCount

	# 연결리스트 원소 삽입
    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1) # 집어넣을 위치 이전 요소를 찾는다.
            newNode.next = prev.next # 새로 넣을 요소 다음 요소 주소에 집어넣을 위치 이전 요소에 
																		 # 입력되어 있던 다음 요소 주소를 넣는다.
            prev.next = newNode      # 이전 요소 다음 요소 주소에 새로운 요소를 넣는다.

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    # 두 연결 리스트 합치기
    def concat(self,L):
        self.tail.next = L.head
        if L.tail:  # L리스트가 비어있지 않은 경우를 제외한다.
            self.tail = L.tail
        self.nodeCount += L.nodeCount
    
    # 특정 노드 지우기
    def popAt(self,pos):
        data=0
        if pos <1 or pos>self.nodeCount:
            raise IndexError
        if pos ==1:
            if pos==self.nodeCount:
                curr=self.head
                self.head=None
                self.tail=None
                data=curr.data
            else:
                curr=self.head
                self.head=curr.next
                data=curr.data
        else:
            if pos==self.nodeCount:
                prev=self.getAt(pos-1)
                curr=prev.next
                prev.next=None
                self.tail=prev
                data=curr.data
            else:
                prev=self.getAt(pos-1)
                curr=prev.next
                prev.next=curr.next
                data=curr.data
        self.nodeCount-=1
        return data

L=LinkedList()
print(L)