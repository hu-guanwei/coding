# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isIdentical(self, one, two):
        """
        input: TreeNode one, TreeNode two
        return: boolean
        """
        # write your solution here

        if (not one) and (not two):
            return True
        elif ((not one) and two) or ((not two) and one):
            return False
        else:
            if one.val != two.val:
                return False
            else:
                return self.isIdentical(one.left, two.left) and self.isIdentical(one.right, two.right)
