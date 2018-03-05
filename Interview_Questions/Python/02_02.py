# Pg 94 - 2.2: Return Kth to Last
# Implement an algorithm to find the kth
# to last element of a singly linked list

from DataStructures.LinkedList import SLLNode

# Concept - Push a runner k away from head node then iterate each
#           until you reach the end of the list
# Big O - Speed O(n) / Memory O(list)

def kToLast(head, k):
    runner1 = head
    runner2 = head

    for _ in range(k):
        if runner2.next != None:
            runner2 = runner2.next
        else:
            print("List not long enough")
            return False

    while runner2.next != None:
        runner1 = runner1.next
        runner2 = runner2.next

    return runner1.value

## Tests
head = SLLNode(1)
head.appendToTail(2)
head.appendToTail(3)
head.appendToTail(4)
print(head)
print(kToLast(head, 0))
print(kToLast(head, 1))
