class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_as_string = ""
        if __name__ == '__main__':
            for row in self.matrix:
                for column in range(len(row)):
                    matrix_as_string += f'{row[column]} '
                matrix_as_string += '\n'
        return matrix_as_string

    def __add__(self, other):
        new_matrix = []
        for first_matrix_row, second_matrix_row in zip(
            self.matrix, other.matrix
        ):
            new_row = []
            for index in range(len(first_matrix_row)):
                sum_of_elements = first_matrix_row[index] + second_matrix_row[index]
                new_row.append(sum_of_elements)
            new_matrix.append(new_row)
        return Matrix(new_matrix)


if __name__ == '__main__':
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(m1)
    print(m2)
    m3 = m1 + m2
    print(m3)
