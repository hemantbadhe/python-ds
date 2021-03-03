"""
    Detect the cycle start point in linked list
    This is the extension of detect cycle in linked list, here once the cycle is detected,
    then assign the slow pointer to self.head and traverse the slow pointer and fast pointer by one(1).
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

    def detect_cycle(self):
        current_node = self.head  # slow pointer
        temp_node = self.head  # fast pointer

        while temp_node and temp_node.next:
            current_node = current_node.next
            temp_node = temp_node.next.next

            if current_node == temp_node:
                print(f"cycle detected")
                current_node = self.head
                break
        else:
            print(f"cycle not detected")
            return

        # now the cycle is detected and now traverse the slow pointer and fast pointer by 1
        while current_node != temp_node:
            current_node = current_node.next
            temp_node = temp_node.next

        print(f"loop starting point: {current_node.data}")


if __name__ == "__main__":
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

    ll.print_list()

    # create a cycle which points last node's next to 4
    """
    1->2->3->4->5->6->7->8->9->|
             ^---------------<-|

    """
    ll.head.next.next.next.next.next.next.next.next.next = ll.head.next.next.next
    ll.detect_cycle()
