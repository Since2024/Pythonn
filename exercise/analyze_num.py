def analyze_numbers(n):
    even_count = 0
    odd_count = 0

    for num in range(1, n + 1):
        if num % 2 == 0:
            print(num, "is Even")
            even_count += 1
        else:
            print(num, "is Odd")
            odd_count += 1

    print("\nSummary:")
    print("Total Even numbers:", even_count)
    print("Total Odd numbers:", odd_count)


# Program starts here
limit = int(input("Enter a number limit: "))
analyze_numbers(limit)
