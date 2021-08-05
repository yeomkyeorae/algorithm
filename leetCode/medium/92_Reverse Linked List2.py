# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        left_lst = lst[:left - 1]
        right_lst = lst[right:]
        center_lst = lst[left - 1:right]
        center_lst = center_lst[::-1]

        lst = left_lst + center_lst + right_lst

        node = ListNode()
        head = node
        for ix, num in enumerate(lst):
            head.val = num
            if ix < len(lst) - 1:
                head.next = ListNode()
                head = head.next

        return node
