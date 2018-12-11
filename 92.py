class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(-1)
        dummy_head.next = head
        pre = dummy_head
        for i in range(m-1):
            pre = pre.next
        cur, reverse = pre.next, None
        for i in range(n-m+1):
            nex = cur.next
            cur.next = reverse
            reverse = cur
            cur = nex
        pre.next.next = cur
        pre.next = reverse
        return dummy_head.next