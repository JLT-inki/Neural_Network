"""
File containing several methods for matrices (aka lists of lists of floats).

Note: There is no Matrix class as it drastically slows the runtime of the
neural network.
"""

def matrix_multiplication(matrix_1: list[list[float]],
                          matrix_2: list[list[float]]) -> list[list[float]]:
    """
    Multiplicate two given matrices.

    Parameters
    ----------
    matrix_1: list[list[float]]
        First matrix of the equation.
    matrix_2: list[list[float]]
        Second matrix of the equation.

    Returns
    -------
    matrix_product: list[list[float]]
        Product of the two given matrices.

    Raises
    ------
    ValueError
        If the number of columns of the first matrix is not equal to the number of
        rows of the second matrix.

    """
    # Check if the two given matrices can be multiplicated
    if len(matrix_1[0]) != len(matrix_2):
        raise ValueError("The two given matrices can't be multiplicated.")

    # Initialize the product of the two given matrices
    matrix_product: list[list[float]] = []

    for row_matrix_1 in range(len(matrix_1)):
        # Add a new line to the product.
        matrix_product.append([])

        for column_matrix_2 in range(len(matrix_2[0])):
            # Multiply row of matrix 1 with column of matrix 2
            matrix_product[row_matrix_1].append(sum([
                matrix_1[row_matrix_1][col_1_row_2]
                * matrix_2[col_1_row_2][column_matrix_2]
                for col_1_row_2 in range(len(matrix_1[0]))]))

    return matrix_product

def matrix_addition(matrix_1: list[list[float]],
                    matrix_2: list[list[float]]) -> list[list[float]]:
    """
    Add the values of two matrices together.

    Parameters
    ----------
    matrix_1: list[list[float]]
        First matrix of the equation.
    matrix_2: list[list[float]]
        Second matrix of the equation.

    Returns
    -------
    matrix_sum: list[list[float]]
        Sum of the two given matrices.

    Raises
    ------
    ValueError
        If the number of columns of the first matrix is not equal to the number of
        rows of the second matrix.

    """
    # Check if the two matrices can be added together
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        raise ValueError("The two given matrices can't be added together")

    matrix_sum = [[matrix_1[row][col] + matrix_2[row][col]
                   for col in range(len(matrix_1[0]))] for row in range(len(matrix_1))]

    return matrix_sum

def invert(matrix: list[list[float]]) -> list[list[float]]:
    """
    Return an inverted matrix.

    Parameters
    ----------
    matrix: list[list[float]]
        The matrix which shall be inverted.

    Returns
    -------
    Matrix(values_inverted): Matrix
        Matrix with inverted values.

    """
    values_inverted: list[list[float]] = []

    for col in range(len(matrix[0])):
        # For each column add a new row
        values_inverted.append([])

        for row in range(len(matrix)):
            values_inverted[col].append(matrix[row][col])

    return values_inverted
