# The Array
numbers = [3, 7, 2, 9, 4]

# Step 1: Assume the first one is the boss
largest = numbers[0]

# Step 2: Look at every number (Logic Loop)
for num in numbers:
    if num > largest:
        largest = num  # Step 3: Update if we find a bigger one

print(f"The largest element is: {largest}")