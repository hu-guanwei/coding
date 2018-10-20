class Solution(object):
    class Node(object):
        def __init__(self, val, next_node=None):
            self.val = val
            self.next = next_node

        def print_all_after(self):
            if self is None:
                print(None)
            while self is not None:
                print(self.val, end=' -> ')
                self = self.next
            print('None')
            return

    #------------------------------------------------
    def find_min(self, head):
        if head is None or head.next is None:
            return head
        curr = head
        min_val = head.val
        min_node = curr
        while curr is not None:
            if curr.val < min_val:
                min_val = curr.val
                min_node = curr
            curr = curr.next
        return min_node

    def selection_sort(self, head):
        if head is None or head.next is None:
            return head
        curr = head
        while curr is not None:
            min_node = self.find_min(curr)
            if min_node.val < curr.val:
                min_node.val, curr.val = curr.val, min_node.val
            curr = curr.next
        return head


node_1 = Solution().Node(1)
node_2 = Solution().Node(2)
node_3 = Solution().Node(3)
node_4 = Solution().Node(4)
node_5 = Solution().Node(5)
node_100 = Solution().Node(100)
node_n_100 = Solution().Node(-100)
node_5.next = node_4
node_4.next = node_3
node_4.next = node_2
node_2.next = node_1
node_1.next = node_100
node_100.next = node_n_100

print('original linked list', end = ': ')
node_5.print_all_after()
#print('min_node.val is ', Solution().find_min(node_5).val)
new_head = Solution().selection_sort(node_5)
print('sorted   linked list', end = ': ')
new_head.print_all_after()

