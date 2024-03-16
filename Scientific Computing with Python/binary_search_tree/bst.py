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
    
    def delete(self, key):
        self.root = self._delete(self.root, key) # assigning a new root to the self.root variable, cause the root can be the key to be deleted, In this case, we need a new root
        
    def _delete(self, node, key):
        if node is None: # if the node was not found, return the node
            return node
        if key < node.key: # if current node is smaller than the key...
            node.left = self._delete(node.left, key) # recursion to the left sub-tree
        elif key > node.key: # else if current node is greater than the key...
            node.right = self._delete(node.right, key) # recursion to the right sub-tree
        else: 
            if node.left is None: #if there's no child on the left...
                return node.right #... return the one on the right
            elif node.right is None: #else if there's no child on the right...
                return node.left #... return the one on the left
            node.key = self._min_value(node.right) # getting the minimim key on the right subtree, so this key can take the deleted key's place
            node.right = self._delete(node.right, node.key) 
        return node
    
    def _min_value(self, node):
        while node.left is not None: # while the nod is not a leaf...
            node = node.left #... keep going down
        return node.key
    
    def inorder_traversal(self):
        result = [] # will store the keys of the nodes in sorted order
        self._inorder_traversal(self.root, result)
        return result
    
    def _inorder_traversal(self, node, result):
        if node: # if node is not empty
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result) # this recursive call explores the entire right subtree in an in-order manner