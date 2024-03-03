class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Function to create a singly linked list
def create_linked_list():
    sll = SinglyLinkedList()
    print("Singly Linked List created successfully.")
    return sll

# Function to append an element to the singly linked list
def append_element(sll):
    if not sll:
        print("Singly Linked List not created yet. Please create linked list first.")
        return
    data = input("Enter element to append to the linked list: ")
    sll.append(data)
    print("Element appended successfully.")

# Function to display the singly linked list
def display_linked_list(sll):
    if not sll:
        print("Singly Linked List not created yet. Please create linked list first.")
        return
    print("Linked List:")
    sll.display()

# Main menu loop
def main():
    sll = None
    while True:
        print("\nSingly Linked List Menu:")
        print("1. Create Singly Linked List")
        print("2. Append Element")
        print("3. Display Singly Linked List")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sll = create_linked_list()
        elif choice == "2":
            append_element(sll)
        elif choice == "3":
            display_linked_list(sll)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
