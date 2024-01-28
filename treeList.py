class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return TreeNode(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append((node.key, node.value))
            self._inorder_traversal(node.right, result)


def main():
    binary_tree = BinaryTree()

    while True:
        print("\nMenu:")
        print("1. Insert into Binary Search Tree")
        print("2. Search in Binary Search Tree")
        print("3. Inorder Traversal")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            key = int(input("Enter the key: "))
            value = input("Enter the value: ")
            binary_tree.insert(key, value)
            print(f"Inserted ({key}, {value}) into the Binary Search Tree.")
        elif choice == '2':
            key = int(input("Enter the key to search: "))
            node = binary_tree.search(key)
            if node:
                print(f"Found: ({node.key}, {node.value})")
            else:
                print(f"Key '{key}' not found in the Binary Search Tree.")
        elif choice == '3':
            traversal_result = binary_tree.inorder_traversal()
            print("Inorder Traversal:")
            for key, value in traversal_result:
                print(f"({key}, {value})")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Wrong choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
