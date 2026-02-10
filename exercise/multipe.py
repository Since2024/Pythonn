# This function prints the multiplication table of a number
def multiplication_table(num, limit):

    # Loop from 1 to limit (inclusive)
    for i in range(1, limit + 1):

        # Multiply the number with the loop variable
        result = num * i

        # Print in a clean format
        print(f"{num} x {i} = {result}")


# ---- Program execution starts here ----

# Take number input from the user
number = int(input("Enter a number: "))

# Take limit input from the user
table_limit = int(input("Enter how far you want the table: "))

# Call the function with both values
multiplication_table(number, table_limit)
