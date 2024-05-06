# linked list pop
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linked_list:
    def __init__(self, value):
        node_baru = Node(value)
        self.head = node_baru
        self.tail = node_baru
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        node_baru = Node(value)
        if self.length == 0:
            self.head = node_baru
            self.tail = node_baru
        else:
            self.tail.next = node_baru
            self.tail = node_baru
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
number = int(input("Input Number: "))
linked_list_saya = linked_list(number)

append_1 = int(input("Append : "))
linked_list_saya.append(append_1)

append_2 = int(input("Append : "))
linked_list_saya.append(append_2)

append_3 = int(input("Append : "))
linked_list_saya.append(append_3)

print("Before Pop ")
linked_list_saya.print_list()

print(linked_list_saya.pop().value)
print(linked_list_saya.pop().value)
print(linked_list_saya.pop())

print("After Pop ")
linked_list_saya.print_list()