"""
    Insert a elemenet in sorted linked list
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

    def insert_node(self, data):
        current_node = self.head
        previous_node = None

        if current_node is None:
            self.push(data)
        while current_node is not None:
            if current_node.data > data:
                break

            previous_node = current_node
            current_node = current_node.next

        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node
        print(f"\nNew node is inserted")


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(6)
    ll.push(5)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    ll.push(0)

    ll.print_list()

    ll.insert_node(4)

    ll.print_list()
