matrix_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


for row in matrix_list:
    for number in row:
        print(number,end=' ')

    print()

print()
matrix_diagonal =[]
matrix_diagonal.append(matrix_list[0][0])
matrix_diagonal.append(matrix_list[1][1])
matrix_diagonal.append(matrix_list[2][2])

print(f"Main diagonal (top-left to bottom-right): {matrix_diagonal}")
