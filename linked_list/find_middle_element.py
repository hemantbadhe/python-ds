"""
    Find the middle element of linked list, 
    if the linked list is even in size, then print the second element
    Ex. linked list is 1->2->3->4->5->6 , then the output should be 4
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

    def get_middle_element(self):
        if not self.head:
            print(f"Empty linked list")

        current_head = self.head
        faster_head = self.head

        while faster_head and faster_head.next:
            current_head = current_head.next
            faster_head = faster_head.next.next
        print(f"middle element in the list: {current_head.data}")


if __name__ == "__main__":
    ll = LinkedList()

    # Adding nodes to linked list
    ll.push(8)
    ll.push(7)
    ll.push(6)
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    ll.push(0)

    # printing the linked list
    ll.print_list()

    # printing the middle element in the linked list
    ll.get_middle_element()
