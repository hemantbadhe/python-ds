"""
	To detect cycle in a linked list(added extra key in node)
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
    ll.push('9')
    ll.push('8')
    ll.push('7')
    ll.push('6')
    ll.push('5')
    ll.push('4')
    ll.push('3')
    ll.push('2')
    ll.push('1')

    # printing the list
    ll.print_list()

    # adding loop
    current_node = ll.head
    # current_node.next.next.next = current_node.next
    ll.head.next.next.next.next.next.next.next.next.next = ll.head.next.next.next

    print(f"Loop detection: ")
    ll.detect_loop()
