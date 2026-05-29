#Display only those characters which are present at an even index number in given string.
word = "pynative"
print("Original String is ", word)

# Method: Using list slicing
# format: [start:stop:step]
even_chars = word[0::2]

print("Printing only even index chars")
for char in even_chars:
    print(char)