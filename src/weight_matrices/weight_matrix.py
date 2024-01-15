"""File containing the WeightMatrix class."""

from __future__ import annotations
from pathlib import Path

import ast
import csv
import _csv

import matrix

class WeightMatrix(matrix.Matrix):
    """
    A class representing one weight matrix. Inherits from the class Matrix.

    Methods
    -------
    write_weights
        Write weight matrices into a CSV file.
    create_weights_from_csv
        Read a CSV file and create a weight matrix per line that is read.

    """

    def __init__(self, values: list[list[float]]) -> None:
        """
        Construct one WeightMatrix object with the given attributes.

        Parameters
        ----------
        weights: list[list[float]]
            List of lists of floats representing individual weights.

        """
        matrix.Matrix.__init__(self, values)

        if self.get_is_vector():
            raise TypeError("Weight matrix can't be a vector.")

    @staticmethod
    def write_weights(path_to_output: str,
                      weight_matrices: list[WeightMatrix]) -> None:
        """
        Write weight matrices into a CSV file.

        Parameters
        ----------
        path_to_output: str
            Path to the CSV file in which the weight matrices need to be written.
        weight_matrices: list[WeightMatrix]
            Altered/New weights that need to be saved.

        Notes
        -----
        Import in line 4 is necessary for type hints of this function as the type
        'WeightMatrix' is used as a forward reference here (see index 563 of the
        Python Enhancement Proposals [PEP 563]).

        """
        # Check if the file exists
        file_exists: bool = Path(path_to_output).is_file()

        # Define the table header
        header: list[str] = ["weights"]

        with open(path_to_output, 'w', encoding='utf-8') as csv_file:
            # Initialize the writer of the CSV file
            csv_writer: _csv._writer = csv.writer(csv_file)

            # Clear the file if it already existed
            if file_exists:
                csv_file.truncate(0)

            # Write the header
            csv_writer.writerow(header)

            # Write each weight matrix
            for weight_matrix in weight_matrices:
                csv_writer.writerow([weight_matrix.get_values()])

    @staticmethod
    def create_weights_from_csv(path_to_csv_file: str) -> list[WeightMatrix]:
        """
        Read a CSV file and create a weight matrix per line that is read.

        Parameters
        ----------
        path_to_csv_file: str
            Path to the CSV file that is read.

        Returns
        -------
        weight_matrix_list: list[WeightMatrix]
            List containing all the weight matrices created.

        Notes
        -----
        Import in line 4 is necessary for type hints of this function as the type
        'WeightMatrix' is used as a forward reference here (see index 563 of the
        Python Enhancement Proposals [PEP 563]).

        """
        # Initialize the return value
        weight_matrix_list: list[WeightMatrix] = []

        with open(path_to_csv_file, 'r', encoding='utf-8') as csv_file:
            # Initialize the reader of the CSV file
            csv_reader: csv.DictReader = csv.DictReader(csv_file)

            # Read each row
            for row in csv_reader:
                # Read the weight matrix & create a WeightMatrix object
                weight_matrix_list.append(WeightMatrix(
                    ast.literal_eval(row["weights"])))

        # Return the newly created WeightMatrix objects
        return weight_matrix_list
