class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next

        if current.next is not None:
            current.next = current.next.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def print_menu():
    print("\nMenu:")
    print("1. Display Linked List")
    print("2. Append to Linked List")
    print("3. Prepend to Linked List")
    print("4. Delete from Linked List")
    print("5. Quit")

def main():
    linked_list = LinkedList()

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            linked_list.display()
        elif choice == '2':
            data = input("Enter the data to append: ")
            linked_list.append(data)
            print(f"Appended '{data}' to the linked list.")
        elif choice == '3':
            data = input("Enter the data to prepend: ")
            linked_list.prepend(data)
            print(f"Prepended '{data}' to the linked list.")
        elif choice == '4':
            data = input("Enter the data to delete: ")
            linked_list.delete(data)
            print(f"Deleted '{data}' from the linked list.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
