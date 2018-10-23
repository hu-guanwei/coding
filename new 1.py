class Solution(object):
	def binarySearch(self, arr, target):
		if arr is None or len(arr) == 0:
			return -1
		l = 0
		r = len(arr) - 1
		while l <= r:
			m = (l + r) // 2
			if target == arr[m]:
				return m
			elif target < arr[m]:
				r = m - 1
			else:
				l = m + 1
		return -1
		
class Solution(object):
	def firstOccur(self, arr, target):
		if arr is None or len(arr) == 0:
			return -1
		l = 0
		r = len(arr) - 1
		while l < r - 1:
			m = (l + r) / 2
			if target == arr[m]:
				r = m
			elif target < arr[m]:
				r = m - 1
			else:
				l = m + 1
		if target == arr[l]:
			return l
		if target == arr[r]:
			return r
		return -1
		
		
class Solution(object):
	def lastOccur(self, arr, target):
		if arr is None or len(arr) == 0:
			return -1
		l = 0
		r = len(arr) - 1
		while l < r - 1:
			m = (l + r) / 2
			if target == arr[m]:
				l = m
			elif target < arr[m]:
				r = m - 1
			else:
				l = m + 1
		if target == arr[r]:
			return r 
		elif target == arr[l]:
			return l 
		return -1
		
class Solution(object):
	def closest(self, arr, target):
		if arr is None or len(arr) == 0:
			return -1
		l = 0
		r = len(arr) - 1
		while l < r - 1:
			m = (l + r) / 2
			if target == arr[m]:
				return m 
			elif target < arr[m]:
				r = m 
			else:
				l = m 
		if abs(target - arr[l]) < abs(target - arr[r]):
			return l 
		return r
	
class Solution(object):
	def kClosest(self, arr, target, k):
		if arr is None or len(arr) == 0:
			return -1
		l = 0
		r = len(arr) - 1
		while l < r - 1:
			m = (l + r) / 2
			if target < arr[m]:
				r = m 
			else:
				l = m 
		cnt = 0
		res = []
		while l >= 0 and r <= len(arr) - 1 and cnt < k:
			if abs(target - arr[l]) < abs(target - arr[r]):
				res.append(arr[l])
				l -= 1
			else:
				res.append(arr[r])
				r += 1
			cnt += 1
		while l >= 0 and cnt < k:
			res.append(arr[l])
			l -= 1
			cnt += 1
		while r <= len(arr) - 1 and cnt < k:
			res.append(arr[r])
			r += 1
			cnt += 1
		return res
		
class Solution(object):
	def search(self, matrix, target):
		l = 0
		n_rows = len(matrix)
		n_cols = len(matrix[0])
		r = n_rows * n_cols - 1
		while l <= r:
			m = (l + r) // 2
			curr_row = m / n_cols
			curr_col = m % n_cols
			if target == matrix[curr_row][curr_col]:
				return [curr_row, curr_col]
			elif target < matrix[curr_row][curr_col]:
				r = m - 1
			else:
				l = m + 1
		return [-1, -1]
		
class Solution(object):
	# merge two sorted LinkedList
	def merge(self, head1, head2):
		if head1 is None and head2 is None:
			return None 
		elif head1 is None:
			return head2
		elif head2 is None:
			return head1
		
		dummy_head = ListNode(0)
		curr = dummy_head
		while head1 is not None and head2 is not None:
			if head1.val < head2.val:
				curr.next = head1
				head1 = head1.next
				curr = curr.next
			else:
				curr.next = head2
				head2 = head2.next
				curr = curr.next
		if head1 is None:
			curr.next = head2
		elif head2 is None:
			curr.next = head1
		return dummy_head.next

class Solution(object):
	def middleNode(self, head):
		if head is None or head.next is None:
			return head
		slow = head
		fast = head
		while fast.next is not None and fast.next.next is not None:
			fast = fast.next.next
			slow = slow.next
		return slow
		