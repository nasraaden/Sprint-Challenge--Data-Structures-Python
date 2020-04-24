from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

# LAST IN, FIRST OUT


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.stack = DoublyLinkedList()

    def push(self, value):
        if value is not None:
            self.stack.add_to_tail(value)
            self.size += 1

    def pop(self):
        if self.stack.tail is not None:
            self.size -= 1
            return self.stack.remove_from_tail()

    def len(self):
        self.size = len(self.stack)
        return self.size
