class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoubleLinkedListMenu:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Method to add a node at the end of the list
    def add(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    # Method to display the menu
    def display_menu(self):
        current = self.head
        print("Menu:")
        while current is not None:
            print("Key:", current.key, ", Value:", current.value)
            current = current.next

def main():
    menu = DoubleLinkedListMenu()

    while True:
        print("\nChoose an option:")
        print("1. Add item")
        print("2. Display Menu")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter key: "))
            value = int(input("Enter value: "))
            menu.add(key, value)
            print("Item added.")
        elif choice == 2:
            menu.display_menu()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
