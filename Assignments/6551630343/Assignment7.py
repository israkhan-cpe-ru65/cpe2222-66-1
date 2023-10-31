import sys
sys.path.append('../../libs/')

import print_utils as printu
import string_utils as stringu

LINE_MAX_LENGTH = 90

def main():
    
    printu.print_repeat_str("*", LINE_MAX_LENGTH, "\n")
    printu.print_centered("Matrix with Tuple", LINE_MAX_LENGTH, "\n")
    printu.print_repeat_str("*", LINE_MAX_LENGTH, "\n")

    (matrix, transpose_matrix) = create_matrix(2, 3)
    
    a_row_i_input = input("Enter row number of the \"A\" matrix:")
    a_col_j_input = input("Enter column number of the \"A\" matrix:")
    a_row_i = int(a_row_i_input) - 1
    a_col_j = int(a_col_j_input) - 1
    
    print(
        stringu.remove_spaces_to_one(
            f"The \"a{a_row_i_input}{a_col_j_input}\" \
            element in the \"A\" matrix is {matrix[a_row_i][a_col_j]}"))
    printu.print_repeat_str("-", LINE_MAX_LENGTH, "\n")

    b_row_i_input = input("Enter row number of the transposed \"A\" matrix:")
    b_col_j_input = input("Enter column number of the transposed \"A\" matrix:")
    b_row_i = int(b_row_i_input) - 1
    b_col_j = int(b_col_j_input) - 1
    
    print(
        stringu.remove_spaces_to_one(
            f"The \"b{b_row_i_input}{b_col_j_input}\" \
            element in the transposed \"A\" matrix is {transpose_matrix[b_row_i][b_col_j]}"))
    printu.print_repeat_str("-", LINE_MAX_LENGTH, "\n")
    
    mulpiplied_matrix = multiply_matrix(matrix, transpose_matrix)

    c_row_i_input = input(
        stringu.remove_spaces_to_one(
            "Enter row number of multiplication of matrices \"A\" \
            and transpose of \"A\":"))
    c_col_j_input = input(
        stringu.remove_spaces_to_one(
            "Enter column number of multiplication of matrices \"A\" \
            and transpose of \"A\":"))
    c_row_i = int(c_row_i_input) - 1
    c_col_j = int(c_col_j_input) - 1
    
    print(
        stringu.remove_spaces_to_one(
            f"The \"c{c_row_i_input}{c_col_j_input}\" element  \
            in multiplication of the \"A\" matrix \
            and the transposed \"A\" matrix is \
            {mulpiplied_matrix[c_row_i][c_col_j]}"))
    printu.print_repeat_str("-", LINE_MAX_LENGTH, "\n")
    # print(matrix)
    # print(transpose_matrix)
    
    
    return


def create_matrix(row = 1, col = 1):
    element = 1
    transpose_matrix = tuple([])
    matrix = tuple([])

    for n in range(1, col + 1):
        j = tuple([])

        for m in range(1, row + 1):
            i = tuple([element])
            j = j + i
            element += 1

        transpose_matrix = transpose_matrix + tuple([j])

    for i in range(0, len(transpose_matrix[0])):
        new_row = tuple([])
        
        for j in range(0, len(transpose_matrix)):
            new_row += tuple([transpose_matrix[j][i]])
        
        matrix += tuple([new_row])
    
    return (matrix, transpose_matrix)


def multiply_matrix(matrix, transpose_matrix):
    multiplied_matrix = tuple([])
    
    for h in range(0, len(transpose_matrix[0])):
        x = tuple([])
        for i in range(0, len(matrix)):
            
            sum = 0
            
            for j in range(0, len(matrix[0])):    
                sum += matrix[i][j] * transpose_matrix[j][h]
                # print(matrix[i][j], "-", transpose_matrix[j][h])
    
            # print(sum)
            x += tuple([sum])

        multiplied_matrix += tuple([x])
            
    # print(multiplied_matrix)
    return multiplied_matrix
    

if __name__ == "__main__":
    main()
