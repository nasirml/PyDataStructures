#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
- Singly linked list common functions generally necessary
- Linked list operations:
    - insert
        - into tail
        - from head
    - display the list
    - count items/nodes in the list
    - circular linked list
        - create the list
        - display the list
    -
TODO:
    - insert after a node
    - delete a node
    -
Created on Mon Jul  2 13:09:57 2018
@author: nasir
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListSingle(object):
    #def __init__(self):
    #    self.head = None

    def insert_into_head(self, list_data):
        '''
        @list_data : List
        @rtype: ListNode, head of the list
        : O(1) running time
        '''
        head = None
        for data in list_data:
            new_node = ListNode(data)
            if head == None:
                head = new_node
            else:
                new_node.next = head
                head = new_node
        return head

    def insert_into_tail(self, list_data):
        '''
        @list_data : List
        @rtype: ListNode, head of the linked list
        : create a linked list from data in a python list
        : return the head of the list which is a node, NOT a list object
        : O(1) for each insertion. It can be O(n) for if we do not use the tail pointer
          just by maintaining an extra node called tail.
        : NOT a doubly linked list. tail just points the last node, thats it. No backward.
        '''
        head = None
        tail = None
        for data in list_data:
            new_node = ListNode(data)
            if head == None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node    # O(1) insert
                tail = tail.next
                #current = head
                #while current.next != None:
                #    current = current.next
                #current.next = new_node
        return head


    def display_list(self, head):
        '''
        @head: ListNode, head of the linked list
        @rtype: None
        '''
        current = head
        while current != None:
            print(str(current.val) + ' -->'),
            current = current.next
        print('')

    def count_nodes(self, head):
        '''
        @head: ListNode, head of the liked list
        @rtype: int, total number of nodes in the linked list
        '''
        current = head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def find_node(self, head, data):
        '''
        @head: ListNode
        @data: node data to find out
        '''
        current = head
        while current != None:
            if current.val == data:
                return True
            current = current.next
        return False

    def circular_linked_list(self, list_data, circle_at):
        '''
        @list_data: list, values should be unique
        @circle_at: int, start of the circle. i.e. tail --> ListNode(circle_at)
        : sometimes we also need circular linked lists to solve some problems.
        : circle is made based on the node value. so its good to have the values
          unique. Otherwise, some comparisons might fail. So be mindful of this.
        '''
        head = None
        circle_node = None
        current = None
        for data in list_data:
            new_node = ListNode(data)
            if data == circle_at:      # keep track of the circle node
                circle_node = new_node
            if head == None:
                head = new_node
            else:
                current = head
                while current.next != None:
                    current = current.next
                current.next = new_node

        current = current.next      # reach to the tail node
        current.next = circle_node  # connect with the one to make circle
        return head

    def display_circular_list(self, head, circle_at):
        '''
        @head: ListNode
        @circle_at: int
        : lets thnk node val are unique
        : increase circle_count each time we encounter the circle_at
        '''
        current = head
        circle_count = 0
        while circle_count != 2:
            if current.val == circle_at:
                circle_count += 1
            print(str(current.val) + ' -->'),
            current = current.next
        print('')
