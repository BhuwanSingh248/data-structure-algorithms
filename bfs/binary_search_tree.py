class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def create(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert(self.root, key)
    
    def insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.val:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        return node
    
    def delete(self, root, key):
        if root is None:
            return root
        
        if key < root.val:
            root.left = self.delete(root.left, key)
        
        elif key > root.val:
            root.right = self.delete(root.right, key)
        
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        return root
    
    def min_value_node(sel, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder_traversal(self, root, arr = []):
        if root is None:
            return root
        self.inorder_traversal(root.left, arr)
        arr.append(root.val)
        self.inorder_traversal(root.right, arr)    
        return arr
    
    def preorder_traversal(self, root, arr=[]):
        if root is None:
            return root
        arr.append(root.val)
        self.preorder_traversal(root.left, arr)
        self.preorder_traversal(root.right, arr)
        return arr

bst = BinarySearchTree()
bst.create(50)
bst.create(30)
bst.create(20)
bst.create(40)
bst.create(70)
bst.create(60)
bst.create(80)

# print("Inorder traversal of the given tree:")
# print(bst.inorder_traversal(bst.root))

print("\nDelete 20:")
bst.delete(bst.root, 20)
print("Inorder traversal of the modified tree:")
print(bst.inorder_traversal(bst.root))
print(bst.preorder_traversal(bst.root))
