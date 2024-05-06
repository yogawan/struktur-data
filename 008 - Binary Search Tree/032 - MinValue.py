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

    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                    temp = temp.left
            elif value > temp.value:
                    temp = temp.right
            else:
                return True
        return False
    
    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def max_value_node(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node

    def reconstruct(self, value, deleteNode, minValueNode):
        if self is None:
            return self
        if value < self.value:
            self.left = deleteNode(self.left, value)
        elif(value > self.value):
            self.right = (deleteNode.right, value)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            temp = minValueNode(self.right)
            self.value = temp.value
            self.right = deleteNode(self.right, temp.value)
        return self