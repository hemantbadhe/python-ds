"""
Find the middle element from linked list
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def find_middle_element(self):
        if self.length == 0:
            print("Linked list is empty")
        else:
            slow_ptr = self.head
            fast_ptr = self.head

            while fast_ptr and fast_ptr.next:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next

            print(f"The middle element is: {slow_ptr.data}")

    def find_middle_element_using_odd_count(self):
        """
        find the middle of linked list using odd number logic, if the count is odd then move forward
        """
        count = 0
        current_head = self.head
        temp_head = self.head

        while temp_head is not None:
            if count & 1:
                current_head = current_head.next
            count += 1
            temp_head = temp_head.next

        print(f"The middle element is: {current_head.data}")

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.data}", end=f"{'->' if current_node.next else ''}")
            current_node = current_node.next
        print("\n")


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_first(60)
    ll.insert_at_first(50)
    ll.insert_at_first(40)
    ll.insert_at_first(30)
    ll.insert_at_first(20)
    ll.insert_at_first(10)

    ll.print_list()

    ll.find_middle_element()
    ll.find_middle_element_using_odd_count()
