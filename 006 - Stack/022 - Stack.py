class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

angka = input("masukan angka: ")
my_stack = Stack(angka)

print("top : ", my_stack.top.value)
print("height : ", my_stack.height)