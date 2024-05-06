# linked list
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


number = int(input("Input Number: "))
linked_list_saya = linked_list(number)

print("Head : ",linked_list_saya.head.value)
print("Tail : ",linked_list_saya.tail.value)
print("Length : ",linked_list_saya.length)