# This function analyzes numbers from 1 to n to check Even or Odd with limit range.
def analyze_numbers(n):

    # Variable to count even and odd numbers
    even_count = 0
    odd_count = 0

    # Loop through numbers from 1 up to n (inclusive)
    for num in range(1, n + 1):

        # Check if the number is divisible by 2
        if num % 2 == 0:
            print(num, "is Even")

            # Increase even counter
            even_count += 1
        else:
            print(num, "is Odd")

            # Increase odd counter
            odd_count += 1

    # This part runs AFTER the loop finishes
    print("\nSummary:")

    # Print total even numbers
    print("Total Even numbers:", even_count)

    # Print total odd numbers
    print("Total Odd numbers:", odd_count)


# Take input from the user and convert it to an integer
limit = int(input("Enter a limit number: "))

# Call the function and pass the input value
analyze_numbers(limit)
