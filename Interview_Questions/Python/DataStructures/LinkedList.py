# Python Version of Linked Lists, Used to help with Interview Questions

####### Singly Linked List
class SLLNode:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

    def appendToTail(self, value):
        end = SLLNode(value)
        runner = self
        while runner.next != None:
            runner = runner.next
        runner.next = end

    def __str__(self):
        if self.next:
            return f"{self.value}->{self.next}"
        return f"{self.value}"

    @staticmethod
    def deleteNode(head, value):
        n = head

        if n.value == value:
            newHead = n.next
            del head
            return newHead

        while n.next != None:
            if n.next.value == value:
                n.next = n.next.next
                return head
            n = n.next

        return head


## SLLNODE TESTS

# head = SLLNode(5)
# head.appendToTail(6)
# head.appendToTail(7)
# head.appendToTail(8)
# print(head)
# head = SLLNode.deleteNode(head, 6)
# print(head)
# head = SLLNode.deleteNode(head, 5)
# print(head)
