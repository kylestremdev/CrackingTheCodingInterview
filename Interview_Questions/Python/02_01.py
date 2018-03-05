# Pg 94 - 2.1: Remove Dups
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP : No Temporary Buffer

from DataStructures.LinkedList import SLLNode

# Part 1 - Use of Hash Table
# Concept - Store seen values in a hash table check each node,
#           if in table delete.
# Big O - Speed O(n) / Memory O(n)

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
head = SLLNode(5)
head.appendToTail(6)
head.appendToTail(5)
head.appendToTail(6)
print(head)
print(removeDups(head))

# Part 2 - No use of extra data structures
