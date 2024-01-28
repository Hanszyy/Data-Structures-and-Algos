def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return 1  # One move is made for a single disk
    moves = 0
    moves += tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    moves += 1  # Move the nth disk
    moves += tower_of_hanoi(n - 1, auxiliary, target, source)
    return moves

# Example usage:
number_of_disks = int(input("Enter the number of disks: "))
total_moves = tower_of_hanoi(number_of_disks, 'A', 'C', 'B')
print(f"\nTotal number of moves: {total_moves}")
