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
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key): 
        if node is None or node.key == key: # if node is None (not present in the tree) or the current node is the one being search, return it
            return node
        if key < node.key: # if the key is smaller than the node...
            return self._search(node.left, key) #... look for it in the left sub-tree   
        return self._search(node.right, key) # else if the key is greater than the node look for it in the right sub-tree