"""
Print the  nth element from last
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            self.length += 1

    def get_element_from_last(self, position):
        """
        length-n+1 approach
        """
        current_node = self.head
        if position > self.length:
            print(f"\nInvalid position")
        else:
            for i in range(0, self.length - position):
                current_node = current_node.next
            print(f"\n{current_node.data}", end="")

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.data}", end=f"{'->' if current_node.next else ''}")
            current_node = current_node.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_last(1)
    ll.insert_at_last(2)
    ll.insert_at_last(3)
    ll.insert_at_last(4)
    ll.insert_at_last(5)

    ll.print_list()

    ll.get_element_from_last(4)
