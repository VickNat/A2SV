class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:
    def __init__(self):
        
        self.headVal = None
        
        return None

    def get(self, index: int) -> int:
        curVal = self.headVal
        idxCounts = 0
        
        if curVal is None:
            return -1
        
        while curVal.next is not None:
            if idxCounts == index:
                break
            
            curVal = curVal.next
            idxCounts += 1
        
        if idxCounts < index:
            return -1
        
        return curVal.value

    def addAtHead(self, val: int) -> None:

        addVal = Node(val)
        
        if self.headVal is None:
            self.headVal = addVal
        else:
            addVal.next = self.headVal
        
            self.headVal = addVal

    def addAtTail(self, val: int) -> None:
        
        addTail = Node(val)
        curVal = self.headVal
        
        
        if self.headVal is None:
            self.headVal = addTail
        else:
            
            while curVal.next is not None:
                curVal = curVal.next
            
            curVal.next = addTail
            

    def addAtIndex(self, index: int, val: int) -> None:
        addIdx = Node(val)
        curVal = self.headVal
        idxCounts = 0
        
        if self.headVal is None and index > 0:
            return
        elif self.headVal is None and index == 0:
            self.headVal = addIdx
        elif self.headVal is not None and index == 0:
            temp = self.headVal
            addIdx.next = temp
            self.headVal = addIdx
        else:
            while curVal.next is not None and idxCounts < index-1:
                curVal = curVal.next
                idxCounts += 1
                
            if idxCounts < index-1:
                return
            
            
            addIdx.next = curVal.next
            curVal.next = addIdx

    def deleteAtIndex(self, index: int) -> None:
        curVal = self.headVal
        idxCounts = 0
        
        if self.headVal is None:
            return
        elif self.headVal.next is None and index == 0:
            self.headVal = None
        elif self.headVal.next is not None and index == 0:
            temp = self.headVal
            self.headVal = self.headVal.next
            temp.next = None
            
            return
            
        while curVal.next is not None and idxCounts < index - 1:
            curVal = curVal.next
            idxCounts += 1
            
        if idxCounts < index - 1:
            return
            
        if curVal.next is None:
            curVal.next = None
            return
        
        if curVal.next.next is None:
            curVal.next = None
        else:
            if curVal.next.next is None:
                curVal.next = None
            else:
                temp = curVal.next
                curVal.next = curVal.next.next
                temp.next = None
                    
            
            

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)