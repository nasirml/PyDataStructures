#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
- driver code to show how to use LinkedListSingleCommon

Created on Tue Jul 24 10:23:08 2018
@author: nasir
"""

from LinkedListSingleCommon import LinkedListSingle


def main():
    list_data = [1,2,3,4,5,6,7,8,9]
    my_list = LinkedListSingle()

    # create the singly linked list
    head = my_list.insert_into_tail(list_data)

    # display it
    my_list.display_list(head)

    # count the number of nodes
    print(my_list.count_nodes(head))

    # etc.

if __name__ == '__main__':
    main()
