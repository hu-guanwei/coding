'''
	   1                         
     /   \         
    2     6
   / \   / \
  3   4  6  6
       \
        5	   
'''		
class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None 	

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.right.left = TreeNode(6)
root.right.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)



def countUnivalSubtrees(root):
    cnt, _ = helper(root)
    return cnt
  
def helper(root):
	if not root:
		return (0, True)
	left_cnt, left_flag = helper(root.left)
	right_cnt, right_flag = helper(root.right)
	
	if left_flag and right_flag:
		if left_cnt == 0 and right_cnt == 0:
			return (1, True)
    
		if left_cnt == 0 and right_cnt != 0:
			if root.right.val == root.val:
				return (right_cnt + 1, True)
			else:
				return (right_cnt, False)
    
		elif left_cnt != 0 and right_cnt == 0:
			if root.left.val == root.val:
				return (left_cnt + 1, True)
			else:
				return (left_cnt, False)
    
		else:
		#left_cnt != 0 and right_cnt != 0:
			if root.val == root.left.val and root.val == root.right.val:
				return (left_cnt + right_cnt + 1, True)
			else:
				return (left_cnt + right_cnt, False)
	else:
		return (left_cnt + right_cnt, False)
		
print(countUnivalSubtrees(root))
