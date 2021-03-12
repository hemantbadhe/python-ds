"""
    Reverse the linked list
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

    def print_reverse(self):
        current_node = self.head
        last_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = last_node
            last_node = current_node
            current_node = next_node
        self.head = last_node

        print(f"The reverse linked list will be, ")
        self.print_list()


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(6)
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    ll.push(0)

    ll.print_list()

    ll.print_reverse()
    ll.print_list()
