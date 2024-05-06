class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

value = int(input("Input Value: "))
my_Doubly_linked_list = DoublyLinkedList(value)

append_1 = int(input("Append: "))
my_Doubly_linked_list.append(append_1)

append_2 = int(input("Append: "))
my_Doubly_linked_list.append(append_2)

append_3 = int(input("Append: "))
my_Doubly_linked_list.append(append_3)

append_4 = int(input("Append: "))
my_Doubly_linked_list.append(append_4)

append_5 = int(input("Append: "))
my_Doubly_linked_list.append(append_5)

print('\nHead, Tail, Length: ')
print('\nHead: ', my_Doubly_linked_list.head.value)
print('Tail: ', my_Doubly_linked_list.tail.value)
print('Length: ', my_Doubly_linked_list.length)

print('\nDoubly Linked List:')
my_Doubly_linked_list.print_list()