# author: yprakash
# https://leetcode.com/problems/reverse-linked-list-ii
# https://leetcode.com/submissions/detail/699704498/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        if head is None or head.next is None or right <= 1:
            return head

        tail = None
        curr = head

        for _ in range(1, left):
            tail = curr
            curr = curr.next

        prev = tail
        tail = curr

        for _ in range(left, right+1):
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn

        if tail.next is None:
            tail.next = curr
            return prev
        else:
            tail.next.next = prev
            tail.next = curr
            return head
