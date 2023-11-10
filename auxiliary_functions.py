"""File containing several auxiliary functions used for the neural network."""

def matrix_multiplication(matrix_1: list[list[float]],
                          matrix_2: list[list[float]]
                          ) -> list[list[float]]:
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
    TypeError
        If one of the two given matrices has lines with different length.
    ValueError
        If the number of columns of the first matrix is not equal to the number of
        rows of the second matrix.

    """
    # Check if all lines of the two given matrices have the same length
    if not matrix_all_rows_same_length(matrix_1):
        raise TypeError("The first given Matrix has rows with different lengths.")
    if not matrix_all_rows_same_length(matrix_2):
        raise TypeError("The second given Matrix has rows with different lengths.")

    # Check if the two given matrices can be multiplicated
    if len(matrix_1[0]) != len(matrix_2):
        raise ValueError("The two given matrices can't be multiplicated.")

    # Initialize the product of the two given matrices
    matrix_product: list[list[float]] = []

    # Multiplicate the two given matrices
    for i, matrix_1_row in enumerate(matrix_1):
        # Add a new line to the product
        matrix_product.append([])

        for j in range(len(matrix_2[i])):
            # Add a 0 as a starting point for the multiplication
            matrix_product[i].append(0)

            for k, number_matrix_1 in enumerate(matrix_1_row):
                matrix_product[i][j] += number_matrix_1 * matrix_2[k][j]

    return matrix_product


def matrix_all_rows_same_length(matrix: list[list[float]]) -> bool:
    """
    Check whether all rows of a given matrix have the same length.

    Parameters
    ----------
    matrix: list[list[float]]
        The matrix that needs to be checked.

    Returns
    -------
    bool
        True if all rows have the same length, otherwise False.

    """
    # Get the length of the first line
    row_length: int = len(matrix[0])

    # Check for all other lines if they have the same length as the first one
    for i in range(1, len(matrix)):
        if len(matrix[i]) != row_length:
            return False

    return True
