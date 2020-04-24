from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check to see if list is full
        size = len(self.storage)
        self.current = self.storage.head
        if size < self.capacity:
            self.storage.add_to_tail(item)
            size += 1
        elif size == self.capacity:
            item = self.current
            self.current += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        self.current = self.storage.head
        while self.current:
            list_buffer_contents.append(self.current.value)
            self.current += 1
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
