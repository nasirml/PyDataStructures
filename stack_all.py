#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
- implementation of basic operations of stack
    - using both linked list and simple python list
- using linked list
- Last in fast out

NOTE:
    - stack can be implemented with a simple python list, say my_stack = []
    - insert at the end/front by my_stack.append(x)
    - remove ALSO from the end/front by my_stack.pop(). That's it!
    - O(1) both push and pop

Created on Thu Jul 12 14:49:44 2018
@author: nasir
"""

class StackNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class StackWithLinkedList(object):
    '''
    : linked list implementation of stack
    : last in first out
      ------------------------------------------->
      start/back (push and pop)           end/front
      ------------------------------------------->
    '''
    def __init__(self):     # an empty top here is not mandatory. just a choice
        self.top = None     # OR, have to return the top from the push function

    def push(self, list_data):
        for data in list_data:
            new_node = StackNode(data)
            new_node.next = self.top
            self.top = new_node

    def display_stack(self):
        if self.top == None: return
        current = self.top
        while current:
            print(str(current.val) + ' -->'),
            current = current.next
        print('')

    def pop(self):
        if self.top == None: return
        value = self.top.val
        self.top = self.top.next
        return value

    def peek(self):
        if self.top == None: return
        return self.top.val

    def is_empty(self):
        return self.top == None


class StackWithSimpleList(object):
    '''
    - very simple to implement!

      ------------------------------------------->
      start/back           end/front (push and pop)
      ------------------------------------------->

    - insert at the end/front by my_stack.append(x)
    - remove ALSO from the end/front by my_stack.pop()
    - O(1) both push and pop
    '''
    def __init__(self):
        self.stack = []

    def stack_push(self, stack_data):
        for data in stack_data:
            self.stack.append(data)

    def display_stack(self):
        if len(self.stack) == 0: return
        for data in self.stack:
            print(str(data) + ' -->'),
        print('')

    def stack_pop(self):
        if len(self.stack) == 0: return
        return self.stack.pop()

def main():
    stack_data = [1,2,3,4,5,6]
    my_stack = StackWithLinkedList()
    my_stack.push(stack_data)
    my_stack.display_stack()
    print(my_stack.pop())
    my_stack.display_stack()
    print('\n')
    my_stack2 = StackWithSimpleList()
    my_stack2.stack_push(stack_data)
    my_stack2.display_stack()
    print(my_stack2.stack_pop())
    my_stack2.display_stack()

if __name__ == '__main__':
    main()

