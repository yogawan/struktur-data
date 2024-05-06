class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

my_tree = BinarySearchTree()

number_1 = input("Input Number: ")
my_tree.insert(number_1)

number_2 = input("Input Number: ")
my_tree.insert(number_2)

number_3 = input("Input Number: ")
my_tree.insert(number_3)

print('Root: ',  my_tree.root.value)
# print('Root Left: ', my_tree.root.left.value) 
print('Root Right: ', my_tree.root.right.value)
# berikan comment di salah satu di antara left atau right