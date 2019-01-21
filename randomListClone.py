# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        mapping = {}
        curr = head
        newHead = None
        prev = None

        while curr:
            cloneNode = RandomListNode(curr.label)
            mapping[curr] = cloneNode
            if prev:
                prev.next = cloneNode
            else:
                newHead = cloneNode
            prev = cloneNode
            curr = curr.next
        
        curr = head
        while curr:
            currRandom = curr.random
            currClone = mapping[curr]
            currCloneRand = None
            if currRandom:
                currCloneRand = mapping[currRandom]
            currClone.random = currCloneRand
            curr = curr.next
        
        return newHead
