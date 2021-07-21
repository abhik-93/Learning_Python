# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        # Initializing prev and res linked lists. Both prev and res point to same memory location.
        # Taking two variable - one to calculate and the other two keep track of the result linkedlist.
        prev = res = ListNode(None)
        carry = 0
        
        while l1 or l2 or carry:

            # If any node of the l1 or l2 is present while other has ended, while will still run and calculate based on carry over

            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
                
            prev.next = ListNode(carry % 10)
            prev = prev.next
            carry //= 10
        
        return res.next  # Since we initially took None as the first node in res.


# Runtime : 64 ms in Leetcode