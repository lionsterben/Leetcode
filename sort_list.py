# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getSize(self, head):
        cnt = 0
        while head is not None:
            head = head.next
            cnt += 1
        return cnt
    
    def split(self, head, length):
        cur = head
        while length > 1 and cur:
            cur = cur.next
            length -= 1
        if cur is None:
            return None
        tmp = cur.next
        cur.next = None
        return tmp
    
    def merge(self, l, r, head):
        cur = head
        while (l and r):
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l if l is not None else r
        while cur.next is not None:
            cur = cur.next
        return cur
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        length = self.getSize(head)
        size = 1
        dummy = ListNode(-1)
        dummy.next = head
        while size < length:
            cur = dummy.next
            tail = dummy
            while cur:
                l = cur
                r = self.split(l, size)
                cur = self.split(r, size)
                tail = self.merge(l, r, tail)
            size *= 2
        return dummy.next