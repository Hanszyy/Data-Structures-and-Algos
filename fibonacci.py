def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoized(n, memo={}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

def main():
    while True:
        print("\nMenu:")
        print("1. Calculate Fibonacci (Recursive)")
        print("2. Calculate Fibonacci (Memoized)")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1' or choice == '2':
            try:
                n = int(input("Enter the value of n: "))
                if n < 0:
                    print("Please enter a non-negative integer.")
                    continue

                if choice == '1':
                    result = fibonacci_recursive(n)
                    print(f"The {n}-th Fibonacci number (Recursive) is: {result}")
                else:
                    result = fibonacci_memoized(n)
                    print(f"The {n}-th Fibonacci number (Memoized) is: {result}")

            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
