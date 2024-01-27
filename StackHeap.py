class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up()

    def extract_min(self):
        if not self.is_empty():
            root = self.heap[0]
            last_element = self.heap.pop()
            if self.heap:
                self.heap[0] = last_element
                self._heapify_down()
            return root
        else:
            raise IndexError("extract from an empty heap")

    def _heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break


def main():
    stack = Stack()
    heap = MinHeap()

    while True:
        print("\nMenu:")
        print("1. Push to Stack")
        print("2. Pop from Stack")
        print("3. Peek Stack")
        print("4. Get Stack Size")
        print("5. Insert into Min Heap")
        print("6. Extract Min from Heap")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            item = input("Enter the item to push: ")
            stack.push(item)
            print(f"{item} pushed to the stack.")
        elif choice == '2':
            try:
                item = stack.pop()
                print(f"Popped item from the stack: {item}")
            except IndexError as e:
                print(str(e))
        elif choice == '3':
            try:
                item = stack.peek()
                print(f"Top item in the stack: {item}")
            except IndexError as e:
                print(str(e))
        elif choice == '4':
            size = stack.size()
            print(f"Size of the stack: {size}")
        elif choice == '5':
            value = int(input("Enter the value to insert into the Min Heap: "))
            heap.insert(value)
            print(f"{value} inserted into the Min Heap.")
        elif choice == '6':
            try:
                min_value = heap.extract_min()
                print(f"Extracted Min from the Min Heap: {min_value}")
            except IndexError as e:
                print(str(e))
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
