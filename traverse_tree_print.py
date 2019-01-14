from binarytree import tree

def preorder(root):
    if not root:
        return
    print(root.value, end=' ')
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.value, end=' ')
    inorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value, end=' ')

root = tree()
print(root)
preorder(root)
print()
inorder(root)
print()
postorder(root)