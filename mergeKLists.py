# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import *

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        prev = None
        curr = None
        start = None
        minHeap = []
        for startNode in A:
            startTuple = (startNode.val, startNode)
            heappush(minHeap,startTuple)
        
        if len(minHeap)>0:
            curr = heappop(minHeap)[1]
        
        while curr != None:
            if prev == None:
                start = curr
            else:
                prev.next = curr
            prev = curr
            currNext = curr.next
            if currNext != None:
                currNextTup = (currNext.val,currNext)
                heappush(minHeap,currNextTup)
            if len(minHeap)>0:
                curr = heappop(minHeap)[1]
            else:
                curr = None
        
        return start

A = [
    [1,5,9,10],
    [2,6],
    [],
    [0,11,12]
]

r = Solution().mergeKLists(A)
print(r)
