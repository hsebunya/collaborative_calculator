"""
A simple calculator that performs additon and multiplication
"""


def get_numbers():
    """Get numbers from user input."""
    numbers = []
    print("Enter numbers (type 'done' when finished ): ")
    while True:
        user_input = input("Enter a number: ").strip()
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input, please enter a valid number.")
    return numbers


def add_numbers():
    pass


def main():
    """Main function to run the calculator."""
    print("=" * 50)
    print("Welcome to the calculator.")
    print("=" * 50)
    numbers = get_numbers()

    if len(numbers) == 0:
        print("No numbers entered exiting.")
        return
    print(f"\n you enetered: {numbers}")
    print("\n What operations would you like to perform?")
    print("1. Add")
    print("2. Multiply")

    choice = input("Enter your choice (1 or 2): ")

# operations will be implemented by Christine and Tricket
    if choice == '1':
        print("Addition feature coming soon")
        # TODO: Tricket to implement this.
    elif choice == '2':
        print("Multiplication feature coming soon.")
        # TODO Christine to implement this.
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
