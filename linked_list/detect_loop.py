"""
	To detect loop in a linked list
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None
        self.flag = False


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
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

    def detect_loop(self):
        current_node = self.head

        while current_node:
            if current_node.flag:
                print(f"Loop detected..!")
                return
            else:
                current_node.flag = True
                current_node = current_node.next


if __name__ == '__main__':
    head = None
    # Adding node in linked list
    ll = LinkedList()
    ll.push(20)
    ll.push(4)
    ll.push(15)
    ll.push(10)

    # printing the list
    ll.print_list()

    # adding loop
    current_node = ll.head
    current_node.next.next.next = current_node.next
    print(f"Loop detection: ")
    ll.detect_loop()
