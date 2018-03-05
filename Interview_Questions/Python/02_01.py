# Pg 94 - 2.1: Remove Dups
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP : No Temporary Buffer

from DataStructures.LinkedList import SLLNode

# Part 1 - Use of Hash Table
# Concept - Store seen values in a hash table check each node,
#           if in table delete.
# Big O - Speed O(n) / Memory O(2n) - Size of list and size of hash table, each O(n)

def removeDups(head):
    if head.next == None: # If only one node there can be no dups
        return head

    d = {}                  # Init Dictionary
    runner = head           # Set runner to head

    while runner.next != None:          # Loop through Linked List
        d[runner.value] = True          # Store runner value in dict
        if runner.next.value in d:      # If runner.next in dict
            temp = runner.next          # Store runner.next for delete
            if runner.next.next != None:        # Skip runner.next if it is dup
                runner.next = runner.next.next
                continue                        # Retry with new runner.next
            else:                       # If no node after runner.next
                runner.next = None      # Break out of loop
                break
            del temp                    # Delete node from memory
        runner = runner.next        # Move to next node

    return head

## Tests
# head = SLLNode(5)
# head.appendToTail(6)
# head.appendToTail(5)
# head.appendToTail(6)
# print(head)
# print(removeDups(head))

# Part 2 - No use of extra data structures
# Concept - Check each node against all the ones after it. (Brute Force)
# Big O - Speed O(n^2) / Memory O(n) - Size of list

def removeDupsSquared(head):
    runner1 = head
    runner2 = runner1.next
    prev = runner1

    while runner1.next != None:
        while runner2 != None:
            if runner2.value == runner1.value:
                prev.next = runner2.next
                del runner2
            else:
                prev = runner2

            runner2 = prev.next

        if runner1.next != None:
            runner1 = runner1.next
            runner2 = runner1.next
            prev = runner1

    return head

## Tests
head = SLLNode(5)
head.appendToTail(6)
head.appendToTail(5)
head.appendToTail(6)
print(head)
print(removeDupsSquared(head))
