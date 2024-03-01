def tower_of_hanoi_visualized(n, source, target, auxiliary):
    towers = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    moves = 0

    def print_towers():
        print("Current state of towers:")
        for rod, disks in towers.items():
            print(f"{rod}: {disks}")

    def move_disk(from_rod, to_rod):
        disk = towers[from_rod].pop()
        towers[to_rod].append(disk)
        print(f"Move disk {disk} from {from_rod} to {to_rod}")
        print_towers()

    def hanoi_recursive(n, source, target, auxiliary):
        nonlocal moves
        if n == 1:
            move_disk(source, target)
            moves += 1
        else:
            hanoi_recursive(n - 1, source, auxiliary, target)
            move_disk(source, target)
            moves += 1
            hanoi_recursive(n - 1, auxiliary, target, source)

    hanoi_recursive(n, source, target, auxiliary)
    return moves

# Example usage:
number_of_disks = int(input("Enter the number of disks: "))
total_moves = tower_of_hanoi_visualized(number_of_disks, 'A', 'C', 'B')
print(f"\nTotal number of moves: {total_moves}")
