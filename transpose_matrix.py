# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(f"Original Matrix: {matrix}")
# print(f"Transposed Matrix: {transposed_matrix}")

def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
            row.append(element)
        matrix.append(row)

    transposed_matrix = transpose_matrix(matrix)

    print(f"Original Matrix:")
    for row in matrix:
        print(row)

    print(f"Transposed Matrix:")
    for row in transposed_matrix:
        print(row)

if __name__ == "__main__":
    main()
