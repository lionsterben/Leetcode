class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def swap(head):
            # print(head.val)
            if head ==  None or head.next == None:
                return head
            temp = head.next.next
            p1, p2 = head, head.next
            p2.next = p1
            p1.next = swap(temp)
            return p2
        return swap(head)

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p1, p2, pre, res = head, head.next, None, head.next
        while p1 != None and p2 != None:
            if pre != None:
                pre.next = p2
            p1.next = p2.next
            p2.next = p1
            if p1.next == None:
                break
            pre = p1
            p1 = p1.next
            p2 = p1.next
        return res