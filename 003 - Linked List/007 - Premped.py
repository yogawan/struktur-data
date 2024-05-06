class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linked_list:
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0: 
            return None
        temp = self.head
        pre= self.head
        while(temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre 
        self.tail.next = None
        self.length -=1

        if self.length == 0:
            self.head = None
            self.tail = None 
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True



number = int(input("Input Number: "))
my_linked_list = linked_list(number)

append_1 = int(input("Append : "))
my_linked_list.append(append_1)

append_2 = int(input("Append : "))
my_linked_list.append(append_2)

append_3 = int(input("Append : "))
my_linked_list.append(append_3)

print('\nBefore Prepend') 
print('----------------')
print('Head: ', my_linked_list.head.value)
print('Tail: ', my_linked_list.tail.value) 
print('Length: ', my_linked_list.length, '\n')

print('Linked List: ')
my_linked_list.print_list()

number_1 = int(input("\nInput Prepend: "))
my_linked_list.prepend(number_1)

print('After Prepend')
print('----------------')
print('Head: ', my_linked_list.head.value)
print('Tail: ', my_linked_list.tail.value)
print('Length: ', my_linked_list.length, '\n')
print('Linked List: ') 
my_linked_list.print_list()