"""
    Basic singly linked list CRUD operation
"""


class Node:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

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

    def insert_at_position(self, position, data):
        if position > self.length < 0:
            print(f"invalid  position.")
            return None
        else:
            if position == 0:
                self.insert_at_beginning(data)
            else:
                if position == self.length:
                    self.insert_at_last(data)
                else:
                    new_node = Node(5)
                    count = 1
                    current_node = self.head
                    while count < position - 1:
                        count += 1
                        current_node = current_node.next
                    new_node.next = current_node.next
                    current_node.next = new_node
                    self.length += 1

    def delete_from_beginning(self):
        if self.head is None:
            print(f"linked list is empty.")
            return None
        else:
            self.head = self.head.next
            self.length -= 1

    def delete_from_last(self):
        if self.head is None:
            print(f"linked list is empty.")
        else:
            current_node = self.head
            prev_node = self.head

            while current_node.next is not None:
                prev_node = current_node
                current_node = current_node.next

            prev_node.next = None
            self.length -= 1

    def delete_at_position(self, position):
        if position > self.length < 0:
            print(f"invalid position.")
            return None
        else:
            if position == 0:
                self.delete_from_beginning()
            else:
                if position == self.length:
                    self.delete_from_last()
                else:
                    current_node = self.head
                    prev_node = self.head
                    count = 0
                    while current_node.next is not None or count < position:
                        count += 1
                        if count == position:
                            prev_node.next = current_node.next
                            self.length -= 1
                            return
                        else:
                            prev_node = current_node
                            current_node = current_node.next

    def clear_list(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print(f"\nLinked list is empty.")
            return
        else:
            current_node = self.head
            while current_node is not None:
                print(f"{current_node.data}", end=f"{'->' if current_node.next else ''}")
                current_node = current_node.next
        print(f"\ntotal length: {self.length}")


if __name__ == "__main__":
    ll = LinkedList()
    # insert at beginning
    print(f"# Inserting 2, 1, 0 at beginning")
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(0)
    ll.print_list()

    # insert at last
    print(f"\n# Inserting 3, 4 at last")
    ll.insert_at_last(3)
    ll.insert_at_last(4)
    ll.print_list()

    # insert at position
    print(f"\n# Inserting 50 at 5th position and 60 at 6th position")
    ll.insert_at_position(5, 50)  # (position, data)
    ll.insert_at_position(6, 60)
    ll.print_list()

    # deleting 0 from beginning
    print(f"\n# Deleting 0 from beginning")
    ll.delete_from_beginning()
    ll.print_list()

    # deleting 60 from last
    print(f"\n# Deleting 60 from last")
    ll.delete_from_last()
    ll.print_list()

    # deleting 60 from last
    print(f"\n# Deleting 4th position element")
    ll.delete_at_position(4)
    ll.print_list()

    # clearing the list
    print(f"\n# clearing the list")
    ll.clear_list()
    ll.print_list()
