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

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    

# input
angka_1 = input("stack: ")
my_stack = Stack(angka_1)
my_stack.print_stack()

angka_2 = input("push: ")
my_stack.push(angka_2)
my_stack.print_stack()

angka_3 = input("push: ")
my_stack.push(angka_3)
my_stack.print_stack()

angka_4 = input("push: ")
my_stack.push(angka_4)
my_stack.print_stack()

# before pop
print("stack before pop ()")
my_stack.print_stack()

# after pop
print("popped node: ")
print(my_stack.pop().value)

print("stack after pop(): ")
my_stack.print_stack()