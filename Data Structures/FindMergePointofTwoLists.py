#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    """
    Finds the node where two singly linked lists merge.

    Args:
        head1: A reference to the head of the first list.
        head2: A reference to the head of the second list.

    Returns:
        The value of the node where the lists merge.
    """
    current1 = head1
    current2 = head2

    while current1 is not current2:
        # If current1 reaches the end of its list, move it to the head of the second list.
        # This effectively makes it traverse the path of list1 + list2.
        if current1 is None:
            current1 = head2
        else:
            current1 = current1.next

        # If current2 reaches the end of its list, move it to the head of the first list.
        # This effectively makes it traverse the path of list2 + list1.
        if current2 is None:
            current2 = head1
        else:
            current2 = current2.next

    # When the loop terminates, current1 and current2 point to the same node,
    # which is the merge point.
    return current1.data

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
            
        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()