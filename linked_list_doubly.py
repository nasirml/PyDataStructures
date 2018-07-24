#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
- doubly linked lists in python
- Operations:
    - insert
        - beginning / end
        - before a node
        - after a node
    - count nodes
    - search
    - display the list
    - delete
    - insert at tail/end

Created on Sat Jun 30 16:05:50 2018
@author: nasir
"""

class Node(object):
    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node
    def get_data(self):
        return self.data
    def get_previous(self):
        return self.prev_node
    def get_next(self):
        return self.next_node
    def set_previous(self, new_prev):
        self.prev_node = new_prev
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedListDouble(object):
    '''
    - bi-directional linked list. keep references of both the prev and next
    - head is the first and tail is the last node
    '''
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_at_tail(self, list_data):
        '''
        @list_data: list
        @rtype: None
        - O(1) time for each insertion
        '''
        for data in list_data:
            new_next = Node(data)
            if self.head == None:
                self.head = new_next
                self.tail = new_next
            else:
                self.tail.set_next(new_next)
                new_next.set_previous(self.tail) # doubly list. set the prev node
                self.tail = new_next

    def insert_after_node(self, data, t_node):
        '''
        @data: node to be inserted
        @t_node: target node, after which insertion will occur
        - insert node data after the t_node, O(n)
        - handle if the t_node is tail node
        '''
        new_node = Node(data)
        current = self.head
        list_tail = self.tail
        if list_tail.data == t_node:
            self.insert_at_tail(data)
        while current != None:
            if current.data == t_node:
                new_node.set_next(current.get_next()) # next of new
                current.get_next().set_previous(new_node)# new_node is the prev of curr->next
                new_node.set_previous(current)        # prev
                current.set_next(new_node)            # doubly list
            current = current.get_next()

    def count_nodes(self):
        '''
        @rtype: int, total number of nodes in the linked list
        - O(n)
        '''
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def display_list(self):
        '''
        - show both from head-->to-->tail and tail-->to-->head
        - O(n)
        '''
        current = self.head
        while current != None:
            print(str(current.data) + ' -->'),
            current = current.get_next()
        print('')
        current = self.tail
        while current != None:
            print(str(current.data) + ' <--'),
            current = current.get_previous()
        print('')


def main():
    '''
    - hey, lets fly from Miami to Atlanta to LA to Dallas etc.
    '''
    list_data = ['mia', 'atl', 'lax', 'ord', 'dfw', 'jfk', 'clt', 'phx', 'dtw']

    # insert in the tail
    my_linked_list = LinkedListDouble()       # head of the list, pointing to nothing
    my_linked_list.insert_at_tail(list_data)

    #my_linked_list.insert_after_node('bos', 'atl') # insert bos after atl
    #my_linked_list.insert_after_node('sfo', 'dfw')

    #count
    print(my_linked_list.count_nodes())

    # display. both from hea-->to-->tail and tail-->to-->head
    my_linked_list.display_list()


if __name__ == '__main__':
    main()

