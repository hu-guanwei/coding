class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def add_two_numbers(self, head1, head2):
        carry = 0
        dummy_head = ListNode(0)
        curr = dummy_head
        while head1 is not None and head2 is not None:
            temp_sum = head1.val + head2.val
            curr.next = Node(temp_sum % 10 + carry)
            carry = temp_sum // 10
            curr = curr.next
            head1 = head1.next
            head2 = head2.next
        if head1 is not None:
            curr.next = head2  
        
