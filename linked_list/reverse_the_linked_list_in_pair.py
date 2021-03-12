"""
    Reverse the linked list in pair
    Example: 1->2->3->4->5->6
    Expected: 2->1->4->3->6->5
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

    def reverse_list_in_pair(self):
        current_code = self.head

        while current_code is not None and current_code.next is not None:
            self.swap_data(current_code, current_code.next)
            current_code = current_code.next.next

    def swap_data(self, node1, node2):
        temp_data = node1.data
        node1.data = node2.data
        node2.data = temp_data


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(6)
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)

    ll.print_list()

    ll.reverse_list_in_pair()

    ll.print_list()
