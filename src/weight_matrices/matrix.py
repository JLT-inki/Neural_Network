"""File containing the matrix class."""

from __future__ import annotations

class Matrix:
    """
    A class representing one matrix.

    Attributes
    ----------
    values: list[int | float] | list[list[int | float]]
        Values stored in the matrix.
    is_vector: bool
        Flag indicating whether the matrix is a vector.

    Methods
    -------
    get_values
        Return the values stored in the matrix.
    get_is_vector
        Indicate whether the matrix is a vector.
    set_values
        Set the values of the matrix.
    set_is_vector
        Set flag indicating whether matrix is a vector.
    get_number_of_rows
        Return the number of rows.
    get_number_of_columns
        Return the number of columns.
    matrix_all_rows_same_length
        Check whether all rows of a given matrix have the same length.
    is_matrix
        Check if given values represent a matrix or a vector.
    matrix_multiplication
        Multiplicate two given matrices.
    invert
        Invert the matrix and overwrite the values.

    """

    def __init__(self, values: list[int | float] | list[list[int, float]]) -> None:
        """
        Construct one Matrix object with the given argument.

        Parameters
        ----------
        values: list[int | float] | list[list[int | float]]
            Values stored in the matrix.

        """
        self.set_values(values)

        # Determine whether matrix is a vector or not and set flag accordingly
        is_vector: bool = isinstance(values[0], (int, float))
        self.set_is_vector(is_vector)

        if not self.is_matrix():
            raise TypeError("Matrix can only contain numbers.")

        if not self.is_vector and not self.matrix_all_rows_same_length():
            raise TypeError("All rows must have the same length.")

    def get_values(self) -> list[int | float] | list[list[int, float]]:
        """
        Return the values stored in the matrix.

        Returns
        -------
        self.values: list[int | float] | list[list[int | float]]
            Values stored in the matrix.

        """
        return self.values

    def get_is_vector(self) -> bool:
        """
        Indicate whether the matrix is a vector.

        Returns
        -------
        self.is_vector: bool
            Returns True if matrix is a vector, otherwise returns False.

        """
        return self.is_vector

    def set_values(self, values: list[int | float] | list[list[int | float]]) -> None:
        """
        Set the values of the matrix.

        Parameters
        ----------
        values: list[int | float] | list[list[int | float]]
            Values stored in the matrix.

        """
        self.values = values

    def set_is_vector(self, is_vector: bool) -> None:
        """
        Set flag indicating whether matrix is a vector.

        Parameters
        ----------
        is_vector: bool
            Flag indicating whether the matrix is a vector.

        """
        self.is_vector: bool = is_vector

    def get_number_of_rows(self) -> int:
        """
        Return the number of rows.

        Returns
        -------
        len(self.get_values()): int
            Number of rows.

        """
        return len(self.get_values())

    def get_number_of_columns(self) -> int:
        """
        Return the number of columns.

        Returns
        -------
        1 | len(self.get_values()[0])
            Number of columns. Is one if the matrix is a vector.

        """
        return 1 if self.get_is_vector() else len(self.get_values()[0])

    def matrix_all_rows_same_length(self) -> bool:
        """
        Check whether all rows of a given matrix have the same length.

        Returns
        -------
        bool
            True if all rows have the same length, otherwise False.

        """
        # Get the length of the first line
        row_length: int = self.get_number_of_columns()

        # Check for all other lines if they have the same length as the first one
        for i in range(1, self.get_number_of_rows()):
            if row_length != len(self.get_values()[i]):
                return False

        return True

    def is_matrix(self) -> bool:
        """
        Check if given values represent a matrix or a vector.

        Returns
        -------
        bool
            Returns True if given values are a matrix or vector,
            otherwise returns False.

        """
        if self.get_is_vector():
            for value in self.get_values():
                if not isinstance(value, (int, float)):
                    return False
        else:
            for row in self.get_values():
                if not isinstance(row, list):
                    return False

                for value in row:
                    if not isinstance(value, (int, float)):
                        return False

        return True

    @staticmethod
    def matrix_multiplication(matrix_1: Matrix, matrix_2: Matrix) -> Matrix:
        """
        Multiplicate two given matrices.

        Parameters
        ----------
        matrix_1: Matrix
            First matrix of the equation.
        matrix_2: Matrix
            Second matrix of the equation.

        Returns
        -------
        matrix_product: Matrix
            Product of the two given matrices.

        Raises
        ------
        ValueError
            If the number of columns of the first matrix is not equal to the number of
            rows of the second matrix.

        Notes
        -----
        Import in line 4 is necessary for type hints of this function as the type
        'Matrix' is used as a forward reference here (see index 563 of the
        Python Enhancement Proposals [PEP 563]).

        """
        # Check if the two given matrices can be multiplicated
        if matrix_1.get_number_of_columns() != matrix_2.get_number_of_rows():
            raise ValueError("The two given matrices can't be multiplicated.")

        # Get the values of both matrices
        values_1: list[int | float] | list[list[int | float]] = matrix_1.get_values()
        values_2: list[int | float] | list[list[int | float]] = matrix_2.get_values()

        # Initialize the product of the two given matrices
        matrix_product: list[list[int | float]] = []

        for i, matrix_1_row in enumerate(values_1):
            # Matrix 1 is vector
            if matrix_1.get_is_vector():
                # Add a new line to the product
                matrix_product.append([])

                for value in values_2[0]:
                    matrix_product[i].append(matrix_1_row * value)
            # Matrix 2 is vector
            elif matrix_2.get_is_vector():
                sum_tmp: int | float = 0

                for j, value in enumerate(values_2):
                    sum_tmp += matrix_1_row[j] * value

                matrix_product.append(sum_tmp)
            else:
                # Add a new line to the product
                matrix_product.append([])

                for j in range(len(values_2[i])):
                    # Add a 0 as a starting point for the multiplication
                    matrix_product[i].append(0)

                    for k, number_matrix_1 in enumerate(matrix_1_row):
                        matrix_product[i][j] += number_matrix_1 * values_2[k][j]

        return Matrix(matrix_product)

    def invert(self) -> None:
        """Invert the matrix and overwrite the values."""
        # The matrix is a vector
        if self.get_is_vector() and self.get_number_of_rows() > 1:
            self.set_values([self.get_values()])
            self.set_is_vector(False)
        # The matrix only has one row
        elif self.get_number_of_rows() == 1:
            self.set_values(list(self.get_values()[0]))
        else:
            original_values: list[list[int | float]] = self.get_values()
            values_inverted: list[list[int | float]] = []

            for col in range(self.get_number_of_columns()):
                # For each column add a new row
                values_inverted.append([])

                for row in range(self.get_number_of_rows()):
                    values_inverted[col].append(original_values[row][col])

            self.set_values(values_inverted)
