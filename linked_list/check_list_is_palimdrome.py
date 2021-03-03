"""
    Check the linked list is palindrome
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
    
    def check_palindrome(self):
        is_palindrome = True
        data_list = []
        
        temp_current_node = self.head
        current_node = self.head

        while temp_current_node is not None:
            data_list.append(temp_current_node.data)
            temp_current_node = temp_current_node.next
        
        while current_node is not None:
            temp = data_list.pop()
            if current_node.data == temp:
               is_palindrome = True
            else:
                is_palindrome = False
                break
            current_node = current_node.next
        return is_palindrome


if __name__ == "__main__":
    ll = LinkedList()
    ll.push('R')
    ll.push('A')
    ll.push('D')
    ll.push('A')
    ll.push('R')

    ll.print_list()

    print(f"is palindrome: {ll.check_palindrome()}")
    