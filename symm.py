# -*- coding: utf-8 -*-
'''
                6
            /       \
           4         4
          / \       / \
         1   5     5   1
        /\   /\   /\  / \
       2  5 8 7  7 8  5  2  
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 检查两棵树是否对称
    def helper(self, root1, root2):
        # 两个 None
        if (not root1) and (not root2):
            return True
        # 一个 None
        elif ((not root1) and root2) or ((not root2) and root1):
            return False
        # 都不为 None
        else:
            if root1.val != root2.val:
                return False
            else:
                return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)
      
  def isSymmetric(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    # write your solution here
    if not root:
        return True
    return self.helper(root.left, root.right)
