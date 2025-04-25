class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        z = Node(data)
        if self.root is None:
            self.root = z
        else:
            temp = self.root
            while True:
                if data < temp.data:
                    if temp.left is None:
                        temp.left = z
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = z
                        break
                    else:
                        temp = temp.right

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

if __name__ == "__main__":
    x = Tree()
    x.insert(10)
    x.insert(20)
    x.insert(7)
    x.insert(12)
    x.insert(30)
    x.insert(13)
    x.insert(9)
    x.insert(6)
    x.insert(11)
    x.insert(41)
    x.insert(25)
    x.insert(5)
    x.insert(8)

    print("\n")
    print("Inorder Traversal:")
    x.inorder(x.root)
    print("\n")
    print("Preorder Traversal:")
    x.preorder(x.root)
    print("\n")
    print("Postorder Traversal:")
    x.postorder(x.root)
    print("\n")