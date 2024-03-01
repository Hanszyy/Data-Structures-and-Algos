class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    pair = (key, value)
                    return
            self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        raise KeyError(f"Key '{key}' not found in the hash table")


def main():
    table_size = int(input("Enter the size of the hash table: "))
    hash_table = HashTable(table_size)

    while True:
        print("\nMenu:")
        print("1. Insert into Hash Table")
        print("2. Get from Hash Table")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            hash_table.insert(key, value)
            print(f"Inserted ({key}, {value}) into the hash table.")
        elif choice == '2':
            key = input("Enter the key to retrieve: ")
            try:
                value = hash_table.get(key)
                print(f"Value for key '{key}': {value}")
            except KeyError as e:
                print(str(e))
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()
