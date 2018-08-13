#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
- Binary search tree, BST

Things implemented:
    - construct bst: iterative
    - inorder traversal
    - search node
    - delete node
Created on Fri Aug 10 13:55:43 2018
@author: nasir
"""

class BSTNode(object):
    # same as the TreeNode
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert_into_bst(self, key):
        '''
        - new values are inserted at leaf
        '''
        current = self.root
        new_node = BSTNode(key)
        if current == None:
            self.root = new_node
            return
        prev = None         # the node to be inserted after this one
        while current != None:
            prev = current
            if key < current.val:
                current = current.left
            else:
                current = current.right
        if key < prev.val:
            prev.left = new_node
        else:
            prev.right = new_node

    def construct_bst(self, tree_data):
        '''
        - root is the first element in the list
        '''
        for item in tree_data:
            self.insert_into_bst(item)
        return self.root

    def bst_inorder(self, current):
        if current == None: return
        self.bst_inorder(current.left)
        print(current.val),
        self.bst_inorder(current.right)

    def search_bst(self, key):
        if self.root == None: return
        current = self.root
        while current != None:
            if key == current.val: return True
            if key < current.val: current = current.left
            else: current = current.right
        return False

    def delete_bst_node(self, key):
        '''
        1. Node to be deleted is leaf: Simply remove from the tree
        2. Node to be deleted has only one child: Copy the child to the node and
           delete the child
        3. Node to be deleted has two children: Find the inorder successor of the node.
           Copy contents of the inorder successor to the node and delete the inorder
           successor.
        - if inorder successor is None then use inorder predecessor
        - inorder successor is the smallest element of the right subtree and inorder
          predecessor is the largest element of the left subtree
        '''
        if self.root == None: return
        current = self.root
        prev = None
        while current != None:
            if current.val == key: break
            #print(current.val),
            prev = current
            if key < current.val:
                current = current.left
            else:
                current = current.right
        if current == None: print('invalid key'); return
        #print(current.val),#; print(prev.val)
        if current.left == None and current.right == None:   # 1. has no children
            if key < prev.val: prev.left = None
            else: prev.right = None
        elif current.left != None and current.right != None: # 3. has two children
            '''
            - find smallest element on the right subtree. go left --> left as dfs, since
              for bst, small values are always at left
            - in-order successor might have a right child. have to copy it in its place
            - keep track of: current = node to be deleted, current2 = victim node
                             prev_tmp = node before the 'victim' node
            '''
            prev_tmp = current
            current2 = current.right
            while current2.left != None:
                prev_tmp = current2
                current2 = current2.left    # victim node
            current.val = current2.val
            #print(current2.val), ; print(prev_tmp.val)
            # put the right subtree of the victim node in its appropriate place or None
            if current2.val < prev_tmp.val:
                prev_tmp.left = current2.right
            else:
                prev_tmp.right = current2.right
        else:
            if current.left != None:
                current.val = current.left.val
                current.left = None
            else:
                current.val = current.right.val
                current.right = None
        return self.root
