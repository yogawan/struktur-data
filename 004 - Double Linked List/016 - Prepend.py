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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

value = int(input("Input Value: "))
my_doubly_linked_list = DoublyLinkedList(value)

append_1 = int(input("Append: "))
my_doubly_linked_list.append(append_1)

append_2 = int(input("Append: "))
my_doubly_linked_list.append(append_2)

append_3 = int(input("Append: "))
my_doubly_linked_list.append(append_3)

append_4 = int(input("Append: "))
my_doubly_linked_list.append(append_4)

append_5 = int(input("Append: "))
my_doubly_linked_list.append(append_5)

print('\nBefore Prepend') 
print('----------------')
print('Head: ', my_doubly_linked_list.head.value)
print('Tail: ', my_doubly_linked_list.tail.value) 
print('Length: ', my_doubly_linked_list.length)

print('\nLinked List: ')
my_doubly_linked_list.print_list()

value = int(input("\nPrepend: "))
my_doubly_linked_list.prepend(value)

print('\nAfter Prepend')
print('----------------')
print('Head: ', my_doubly_linked_list.head.value)
print('Tail: ', my_doubly_linked_list.tail.value)
print('Length: ', my_doubly_linked_list.length)

print('\nLinked List: ') 
my_doubly_linked_list.print_list()