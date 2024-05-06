class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

angka_1 = input("queue: ")
my_queue = Queue(angka_1)

# before enqueue
print("before enqueue")
my_queue.print_queue()

# after enqueue
angka_2 = input("enqueue: ")
my_queue.enqueue(angka_2)
print("after enqueue")
my_queue.print_queue()