#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
- simple queue implementation using linked list
    - implemented in both linked list and simple python list
- can be done with simple list too
- first in first out
- layeout relative first one is implemented here:
- using doubly linked list

      ------------------------------------------->
      start/back (push)              end/front (pop)
      ------------------------------------------->


NOTE:
    - queue can be implemented with a simple python list, say my_queue = []
    - insert at the start/back by my_queue.insert(0, x)
    - remove from the end/front by my_queue.pop(). Thats it!
    - O(n) push and O(1) pop

Created on Fri Jul 13 11:02:22 2018
@author: nasir
"""

class QueueNode(object):
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None

class QueueWithLinkedList(object):
    '''
    : simple queue implementaion with simple list
    : first in first out
    : push from the back and pop from the front
    '''
    def __init__(self):
        self.front = None
        self.back = None

    def push(self, list_data):
        # front never changes (unless pop). take the back to the left (further back!)
        for data in list_data:
            new_node = QueueNode(data)
            if self.back == None:   # queue is empty
                self.back = new_node
                self.front = new_node
            else:
                new_node.next = self.back
                self.back.prev = new_node
                self.back = new_node

    def display_queue(self):
        if self.back == None: return
        current = self.back
        while current != None:
            print(str(current.val) + ' -->'),
            current = current.next
        print('')

    def pop(self):
        # pick, set front, and remove the old front
        if self.front == None: return
        value = self.front.val
        self.front = self.front.prev
        self.front.next = None
        return value

    def peek(self):
        if self.back == None: return
        return self.front.val

    def is_empty(self):
        return self.back == None


class QueueWithSimpleList(object):
    '''
    - very easy to implement with python list!
    - insert at the start/back by my_queue.insert(0, x)
    - remove from the end/front by my_queue.pop(). Thats it!
    - O(n) push and O(1) pop
    '''
    def __init__(self):
        self.queue = []

    def queue_push(self, queue_data):
        for data in queue_data:
            self.queue.insert(0, data)

    def display_queue(self):
        if len(self.queue) == 0: return
        for data in self.queue:
            print(str(data) + ' -->'),
        print('')

    def stack_pop(self):
        if len(self.queue) == 0: return
        return self.queue.pop()

def main():
    queue_data = [1,2,3,4,5,6]
    my_queue = QueueWithLinkedList()
    my_queue.push(queue_data)
    my_queue.display_queue()
    print(my_queue.pop())
    my_queue.display_queue()
    print('\n')
    my_queue2 = QueueWithSimpleList()
    my_queue2.queue_push(queue_data)
    my_queue2.display_queue()
    print(my_queue2.stack_pop())
    my_queue2.display_queue()


if __name__ == '__main__':
    main()
