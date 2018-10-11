# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def get_len(head):
            count = 0
            while head != None:
                count += 1
                head = head.next
            return count
        count_a = get_len(headA)
        count_b = get_len(headB)
        cat_a = headA
        cat_b = headB
        if count_a >= count_b:
            forward = count_a - count_b
            print(forward)
            while forward > 0:
                cat_a = cat_a.next
                forward -= 1
            while cat_a != None and cat_b != None:
                if cat_a == cat_b:
                    return cat_a
                cat_a = cat_a.next
                cat_b = cat_b.next
        else:
            forward = count_b - count_a
            while forward > 0:
                cat_b = cat_b.next
                forward -= 1
            while cat_a != None and cat_b != None:
                if cat_a == cat_b:
                    return cat_a
                cat_a = cat_a.next
                cat_b = cat_b.next
        return None