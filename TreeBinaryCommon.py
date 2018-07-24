#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
- NOT a BST, just binary tree. That is there is no sorted order on the values
  in any way.
- You can use this as import in your code to create, display the tree while you
  are doing some other operations on binary trees.
- Things implemented:
    - create/construct the tree
    - Display/Traverse (in-order, pre-order, post-order)
    - search for a node
TODO:
    - delete/remove a node
    -

Created on Fri Jul 13 14:21:13 2018
@author: nasir
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree(object):
    #def __init__(self):
    #    self.root = None

    def insert_into_tree(self, tree_data):
        '''
        @tree_data: list, of numbers
        @rtype: TreeNode, root of the tree
        : scan the list and construct the tree on the fly.
        : do level order traversal until we find an empty space
        : we need to store left and right node of a node for later processing
        : so we store them in a Queue for sequential placement.
        : put both left and right at once so that a node can have only right child
        : following the code in leetCode tree problems!
        '''
        root = TreeNode(int(tree_data[0]))
        node_queue = [root]
        idx = 1         # root is idx = 0
        while idx < len(tree_data):
            node = node_queue.pop()

            item = tree_data[idx]
            idx = idx + 1
            if item != None:
                left_number = int(item)
                node.left = TreeNode(left_number)
                node_queue.insert(0, node.left)

            if idx >= len(tree_data): break

            item = tree_data[idx]
            idx = idx + 1
            if item != None:
                right_number = int(item)
                node.right = TreeNode(right_number)
                node_queue.insert(0, node.right)
        return root

    def display_inorder(self, current):
        # O(n) time
        if current == None: return
        self.display_inorder(current.left)
        print(str(current.val) + ' '),
        self.display_inorder(current.right)

    def display_preorder(self, current):
        # O(n) time
        if current == None: return
        print(str(current.val) + ' '),
        self.display_preorder(current.left)
        self.display_preorder(current.right)

    def display_postorder(self, current):
        # O(n) time
        if current == None: return
        self.display_postorder(current.left)
        self.display_postorder(current.right)
        print(str(current.val) + ' '),


    def search_binary_tree(self, current, key):
        '''
        : same as insertion. level order iterative search using a queue
        : O(n), its NOT a BST, so we have to search the entire tree
        '''
        if current == None: return False
        node_queue = []
        node_queue.insert(0, current)
        while len(node_queue) > 0:
            tmp = node_queue.pop()
            if tmp.val == key:
                return True
            if tmp.left != None:
                node_queue.insert(0, tmp.left)
            if tmp.right != None:
                node_queue.insert(0, tmp.right)
        return False
