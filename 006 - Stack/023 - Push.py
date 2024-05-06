class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

# before push
angka_1 = input("masukan angka: ")
my_stack = Stack(angka_1)

print("stack before push: ")
my_stack.print_stack()

# after push
angka_2 = input("masukan angka: ")
my_stack.push(angka_2)

print("stack after push: ")
my_stack.print_stack()