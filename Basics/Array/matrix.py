# Function to take 3x3 matrix input from user
def input_matrix():

    matrix = []  # empty list to store rows

    # Loop for 3 rows
    for i in range(3):
        row = list(map(int, input(f"Enter row {i+1} (3 numbers separated by space): ").split()))
        matrix.append(row)  # add row to matrix

    return matrix


# Function to add two matrices
def add_matrices(mat1, mat2):

    result = []  # this will store the result matrix

    # Loop through rows
    for i in range(3):

        row = []

        # Loop through columns
        for j in range(3):

            # Add corresponding elements
            row.append(mat1[i][j] + mat2[i][j])

        result.append(row)

    return result


# Function to print matrix nicely
def print_matrix(matrix):

    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()


print("Enter Matrix A")
A = input_matrix()

print("\nEnter Matrix B")
B = input_matrix()

# Add matrices
C = add_matrices(A, B)

print("\nResult Matrix (A + B):")
print_matrix(C)