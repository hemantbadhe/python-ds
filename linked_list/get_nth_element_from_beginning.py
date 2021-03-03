"""
    Find nth element in the list from beginning
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def print_list(self):
        current_node = self.head

        while current_node:
            print(f"{current_node.data} ->", end="")
            current_node = current_node.next
        print(f"\n")

    def get_nth_element_from_beginning(self, position):
        if self.length < position:
            print(f"Invalid position.")
            return

        current_node = self.head
        count = 0
        while current_node:
            if position == count:
                print(f"{position}th element from beginning: {current_node.data}")
                return
            else:
                current_node = current_node.next
                count += 1


if __name__ == "__main__":
    ll = LinkedList()

    # Adding node in list
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    ll.push(0)

    # printing the linked list
    ll.print_list()

    # printing the nth element from beginning
    ll.get_nth_element_from_beginning(5)
