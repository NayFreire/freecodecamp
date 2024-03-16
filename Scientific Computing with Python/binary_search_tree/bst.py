class TreeNode:
    def __init__(self, key): #key is the value to be stored in the node
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None: # a new node can only be inserted in a leaf (None assinged position)
            return TreeNode(key)
        if key < node.key: # if the key is smaller than the current node, if should be inserted to the left of this node
            node.left = self._insert(node.left, key)
        elif key > node.key: # if the key is greater than the current node, if should be inserted to the right of this node
            node.right = self._insert(node.right, key)
        
        return node
    
        