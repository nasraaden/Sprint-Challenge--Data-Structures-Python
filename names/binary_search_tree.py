from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check to see if there is a node (either left or right)
        # check to see if value inserting is less than or greater than value at the root
        # if it is, check to see if right or left is none
        # if not none, insert value at right or left
        # if none, put the value there with a new instance of BST
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is None:
            return False
        elif target == self.value:
            return True
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call the function cb on self.value
        cb(self.value)
        # call for each on the right side so it can call cb on each value
        if self.right:
            self.right.for_each(cb)
        # call for each on the left side so it can call cb on each value
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return

        if node.left is not None:
            node.in_order_print(node.left)

        print(node.value)

        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # using queue so we need a new instance of queue
        queue = Queue()
        # add the root to the queue
        queue.enqueue(node)
        # while queue is not empty
        while queue.size != 0:
            # delete the head of the queue
            deleted = queue.dequeue()
            # print that
            print(deleted.value)
            # check to see if deleted node has children on the left
            if deleted.left is not None:
                # add left child to queue
                queue.enqueue(deleted.left)
            # check to see if deleted node has children on the right
            if deleted.right is not None:
                # add right child to queue
                queue.enqueue(deleted.right)

    # while node
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # using stack so we need a new instance of stack
        stack = Stack()
        # add node to stack
        stack.push(node)
        # while stack is not empty
        while stack.size != 0:
            # delete the node from the stack
            deleted = stack.pop()
            # print it
            print(deleted.value)
            # check to see if deleted node has children on the right
            if deleted.right is not None:
                stack.push(deleted.right)
            # check to see if deleted node has children on the left
            if deleted.left is not None:
                stack.push(deleted.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
