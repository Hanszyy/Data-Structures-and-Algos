import os

class Note:
    def __init__(self, content):
        self.content = content
        self.next = None

class NotesList:
    def __init__(self):
        self.head = None

    def add_note(self, content):
        new_note = Note(content)
        new_note.next = self.head
        self.head = new_note

    def list_notes(self):
        current = self.head
        while current is not None:
            print(current.content)
            current = current.next

    def save_to_file(self, filename):
        directory = "Note Files"
        if not os.path.exists(directory):
            os.makedirs(directory)

        filepath = os.path.join(directory, filename)

        with open(filepath, 'w') as file:
            current = self.head
            while current is not None:
                file.write(current.content + '\n')
                current = current.next
            print(f"Notes saved to '{filepath}'")

def print_menu():
    print("\nMenu:")
    print("1. Take Note")
    print("2. List Notes")
    print("3. Save to File")
    print("4. Quit")

def main():
    notes_list = NotesList()

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            note_content = input("Enter your note: ")
            notes_list.add_note(note_content)
            print("Note added.")
        elif choice == '2':
            print("Your Notes:")
            notes_list.list_notes()
        elif choice == '3':
            filename = input("Enter the filename to save notes: ")
            notes_list.save_to_file(filename)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
