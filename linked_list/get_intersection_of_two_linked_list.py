"""
    Find the intersection node of two linked list
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        current_node = self.head

        while current_node:
            print(f"{current_node.data} ->", end="")
            current_node = current_node.next
        print(f"\n")

    def get_the_intersection(self, list1, list2):
        list1_length = 0
        list2_length = 0

        list1_head = list1
        list2_head = list2

        while list1_head is not None:
            list1_length += 1
            list1_head = list1_head.next

        while list2_head is not None:
            list2_length += 1
            list2_head = list2_head.next

        current_list1 = list1
        current_list2 = list2

        if list1_length > list2_length:
            for _ in range(list1_length - list2_length):
                current_list1 = current_list1.next

        if list1_length < list2_length:
            for _ in range(list2_length - list1_length):
                current_list2 = current_list2.next

        while current_list1 != current_list2:
            current_list1 = current_list1.next
            current_list2 = current_list2.next

        print(f"\nLinked list intersects at node: {current_list1.data}")


if __name__ == "__main__":
    # linked list 1
    print("linked list 1")
    l1 = LinkedList()
    l1.push(30)
    l1.push(15)
    l1.push(9)
    l1.push(6)
    l1.push(3)

    l1.print_list()

    # linked list 2
    print("linked list 2")
    l2 = LinkedList()
    l2.push(30)
    # l2.push(15)
    # l2.push(10)

    l2.print_list()

    # creating the intersection
    print("linked list 2 after the intersection")
    l2.head.next = l1.head.next.next.next

    l2.print_list()

    ll = LinkedList()
    ll.get_the_intersection(l1.head, l2.head)
