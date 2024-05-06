import os

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
        return True
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


def queue():
    angka_1 = input("Queue: ")
    my_queue = Queue(angka_1)

    print("Queue are: ")
    my_queue.print_queue()

def enqueue():
    angka_1 = input("Queue: ")
    my_queue = Queue(angka_1)

    # before enqueue
    print("Before Enqueue")
    my_queue.print_queue()

    # after enqueue
    angka_2 = input("Enqueue: ")
    my_queue.enqueue(angka_2)
    print("After Enqueue")
    my_queue.print_queue()

def dequeue():
    angka_1 = input("Queue: ")
    my_queue = Queue(angka_1)

    # before enqueue
    print("Before Dequeue")
    my_queue.print_queue()

    # after enqueue
    angka_2 = input("Dequeue: ")
    my_queue.enqueue(angka_2)
    print("After Dequeue")
    my_queue.print_queue()

    print("Dequeue")
    print(my_queue.dequeue().value)
    print(my_queue.dequeue().value)
    print(my_queue.dequeue())

def showHeader():
        print(f"{'Menu':^50}")
        print("-"*60)
        print(f"1. Fungsi Queue") # clear
        print(f"2. Fungsi Enqueue") # clear
        print(f"3. Fungsi Dequeue") # clear
        print(f"4. Exit") # clear

if __name__ == "__main__":
    sistem_operasi = os.name
    while(True):
        showHeader()
        print("-"*60)
        user_option = input("Input Number: ")
        print("-"*60)

        match user_option:
            case "1":
                  queue()
            case "2":
                  enqueue()
            case "3":
                  dequeue()
            case "4":
                break

        print("-"*60)

    print("Program berakhir, Terimakasih")