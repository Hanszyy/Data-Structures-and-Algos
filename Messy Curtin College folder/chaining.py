class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class ChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        if current is None:
            return  # Key not found
        if current.key == key:
            self.table[index] = current.next
        else:
            while current.next is not None and current.next.key != key:
                current = current.next
            if current.next is not None:
                current.next = current.next.next

    def display_all(self):
        print("\nHash Table:")
        for index, node in enumerate(self.table):
            print(f"Index {index}: ", end="")
            while node is not None:
                print(f"({node.key}, {node.value})", end=" -> ")
                node = node.next
            print("None")

def print_menu():
    print("\nMenu:")
    print("1. Insert into Hash Table")
    print("2. Search in Hash Table")
    print("3. Delete from Hash Table")
    print("4. Display All Entries in Hash Table")
    print("5. Quit")

def main():
    table_size = int(input("Enter the size of the hash table: "))
    hash_table = ChainingHashTable(size=table_size)

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            hash_table.insert(key, value)
            print(f"Inserted ({key}, {value}) into the hash table.")
        elif choice == '2':
            key = input("Enter the key to search: ")
            result = hash_table.search(key)
            if result is not None:
                print(f"Found: ({key}, {result})")
            else:
                print(f"Key '{key}' not found in the hash table.")
        elif choice == '3':
            key = input("Enter the key to delete: ")
            hash_table.delete(key)
            print(f"Deleted key '{key}' from the hash table.")
        elif choice == '4':
            hash_table.display_all()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
