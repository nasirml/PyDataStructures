#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
- driver program to use TreeBinaryCommon

Created on Tue Jul 24 12:40:11 2018
@author: nasir
"""


from TreeBinaryCommon import BinaryTree

def main():
    '''
    - Here is how you use the tree in your program. make sure you import the
      BinaryTree class
    - data starts from the root and fills up from the left. 'None' indicates
      no child on that branch anymore.
    '''
    # construct the tree
    tree_data = [1,2,3,0,7,5,9,8,10,0,2]
    #tree_data = [1,2,2,None,3,None,3]
    my_tree = BinaryTree()
    root = my_tree.insert_into_tree(tree_data)

    # display/traverse
    my_tree.display_inorder(root)
    print('')
    #my_tree.display_preorder(root); print('')
    #my_tree.display_postorder(root); print('')

    # search
    #key = 10
    #print(my_tree.search_binary_tree(root, key))


if __name__ == '__main__':
    main()