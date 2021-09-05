# Time complexity : O(n)
# Space complexity : O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def removeDuplicates(self):
        temp = self.head
        while temp.next:
            if temp.data != temp.next.data:
                temp = temp.next

            else:
                temp.next = temp.next.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next
        print()




ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(30)
ll.head.next.next.next.next = Node(50)
ll.head.next.next.next.next.next = Node(50)

ll.printList()
ll.removeDuplicates()
ll.printList()