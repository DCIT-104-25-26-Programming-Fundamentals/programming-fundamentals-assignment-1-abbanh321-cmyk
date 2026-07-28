# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

def calculate_sum(numbers):
    total = 0
    for value in numbers:
        total += value
    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_max(numbers):
    maximum = numbers[0]
    for value in numbers[1:]:
        if value > maximum:
            maximum = value
    return maximum


def calculate_min(numbers):
    minimum = numbers[0]
    for value in numbers[1:]:
        if value < minimum:
            minimum = value
    return minimum


def main():
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: N must be a positive integer.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    numbers = []
    for i in range(1, n + 1):
        try:
            value = int(input(f"Enter number {i}: "))
        except ValueError:
            print("Please enter a valid integer.")
            return
        numbers.append(value)

    print()
    print("Results:")
    print(f"Sum:     {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers):.1f}")
    print(f"Maximum: {calculate_max(numbers)}")
    print(f"Minimum: {calculate_min(numbers)}")


if __name__ == "__main__":
    main()

