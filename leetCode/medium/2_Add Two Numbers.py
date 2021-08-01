# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp_d1 = collections.deque()
        while l1:
            tmp_d1.append(l1.val)
            l1 = l1.next

        tmp_d2 = collections.deque()
        while l2:
            tmp_d2.append(l2.val)
            l2 = l2.next

        str_l1 = ''
        while tmp_d1:
            str_l1 += str(tmp_d1.pop())

        str_l2 = ''
        while tmp_d2:
            str_l2 += str(tmp_d2.pop())

        str_sum = str(int(str_l1) + int(str_l2))
        str_sum = str_sum[::-1]

        answer = ListNode(int(str_sum[0]))
        header = answer
        for ch in str_sum[1:]:
            point = ListNode(int(ch))
            header.next = point
            header = point

        return answer
