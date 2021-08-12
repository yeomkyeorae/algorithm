# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next

        answer = ListNode()
        head = answer
        while heap:
            new_node = ListNode(heapq.heappop(heap))
            head.next = new_node
            head = head.next

        return answer.next
