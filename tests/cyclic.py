# detect cycle in linked list

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count+=1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getValue() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getValue() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def hasLoop(self):
        current = self.head
        if current is None:
            return False
        slow = fast = current
        loop = None
        while loop is None:
            if slow.getNext() is not None:
                slow = slow.getNext()
            else:
                loop = False
            if fast.getNext().getNext() is not None:
                fast = fast.getNext().getNext()
            else:
                loop = False
                '''
            if slow.getNext() is None or fast.getNext() is None:
                return False
                '''
            if slow is fast:
                loop = True
        return loop

myList = UnorderedList()
print(myList.isEmpty())
print(myList.size())
myList.add(6)
myList.add(5)
myList.add(4)
myList.add(3)
myList.add(2)
myList.add(1)
print(myList.isEmpty())
print(myList.size())
print(myList.search(99))
print(myList.size())
print(myList.hasLoop())
last = myList.getHead().getNext().getNext().getNext().getNext().getNext()
print(last.getValue())
last.setNext(myList.getHead())
print(myList.hasLoop())
