# Function to create an array
def create_array():
    array = []
    print("Array created successfully.")
    return array

# Function to add elements to the array
def add_elements(array):
    element = input("Enter element to add to the array: ")
    array.append(element)
    return array

# Function to display the array
def display_array(array):
    if array:
        print("Array:", array)
    else:
        print("Array not created yet. Please create array first.")

# Function to append an element to the end of the array
def append_element(array, element):
    if array is None:
        print("Array not created yet. Please create array first.")
        return array
    else:
        array.append(element)
        return array

# Main menu loop
def main():
    array = None
    while True:
        print("\nArray Menu:")
        print("1. Create Array")
        print("2. Add Elements")
        print("3. Display Array")
        print("4. Add element to end of array")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            array = create_array()
        elif choice == "2":
            array = add_elements(array)
        elif choice == "3":
            display_array(array)
        elif choice == "4":
            if array:
                element = input("Enter element to add to the end of the array: ")
                array = append_element(array, element)
            else:
                print("Array not created yet. Please create array first.")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
