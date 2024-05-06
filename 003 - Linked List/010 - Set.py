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

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False



number = int(input("Input Number: "))
my_linked_list = linked_list(number)

append_1 = int(input("Append : "))
my_linked_list.append(append_1)

append_2 = int(input("Append : "))
my_linked_list.append(append_2)

append_3 = int(input("Append : "))
my_linked_list.append(append_3)

print('Before set_value(): ')
my_linked_list.print_list()

index = int(input("Input Index: "))
value = int(input("Input Value: "))
my_linked_list.set_value(index,value)

print('After set_value(): ')
my_linked_list.print_list()