"""
    Search an element in a Linked List 
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

    # Approach 1
    def search_elemet(self, element):
        if self.head is None:
            print(f"Empty linked list")
        else:
            current_node = self.head
            while current_node:
                if current_node.data == element:
                    print(f"Element found")
                    return
                else:
                    current_node = current_node.next
            else:
                print(f"Element not found in list")

    # Approach 2
    def search_element_rec(self, head, element):
        if not head:
            print(f"Element not found in list")
            return

        if head.data == element:
            print(f"Element found")
        else:
            return self.search_element_rec(head.next, element)


if __name__ == "__main__":
    ll = LinkedList()

    # adding nodes in linkedlist
    ll.push(5)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    ll.push(0)

    # printing the linkedlist
    ll.print_list()

    # finding element in linkedlist
    ll.search_elemet(50)

    # finding element in linkedlist using recursive function
    ll.search_element_rec(ll.head, 50)
