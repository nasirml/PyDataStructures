#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

Created on Mon Aug 13 16:10:17 2018
@author: nasir
"""

from TreeBSTCommon import BST

def main():
    #tree_data = [8,3,1,10,6,4,7,14,13]
    #tree_data = [100,20,10,30,500,40, 200,300,600]
    tree_data = [100,50,200,30,70,150,250,20,60,170,55]
    my_bst = BST()
    bst_root = my_bst.construct_bst(tree_data)
    my_bst.bst_inorder(bst_root); print('')
    print(my_bst.search_bst(200))
    my_bst.delete_bst_node(70)
    my_bst.bst_inorder(bst_root); print('')

if __name__ == '__main__':
    main()
