'''
6. Determine if a binary tree is a binary search tree
Given a Binary Tree, figure out whether it’s a Binary Search Tree. In a binary search tree, each 
node’s key value is smaller than the key value of all nodes in the right subtree, and is greater than 
the key values of all nodes in the left subtree. Below is an example of a binary tree that is a valid BST.
'''

def is_bst_rec(root, min_val, max_val):
  if root == None:
    return True

  if root.data < min_val or root.data > max_val:
    return False
  
  return is_bst_rec(root.left, min_val, root.data) and is_bst_rec (root.right, root.data, max_val)

def is_bst(root):
  return is_bst_rec(root, -sys.maxsize-1, sys.maxsize)

#tested in browser