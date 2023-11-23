"""File containing the weight class."""

# Imports necessary for the write_weights method
from __future__ import annotations
from pathlib import Path

import csv
import _csv

class WeightMatrix:
    """
    A class representing one weight matrix.

    Attributes
    ----------
    weights: list[list[float]]
        List of lists of floats representing individual weights.

    Methods
    -------
    get_weights
        Return the weight matrix.
    write_weights
        Write weight matrices into a CSV file.

    """

    def __init__(self, weights: list[list[float]]) -> None:
        """
        Construct one WeightMatrix object with the given attributes.

        Parameters
        ----------
        weights: list[list[float]]
            List of lists of floats representing individual weights.

        """
        self.weights = weights

    def get_weights(self) -> list[list[float]]:
        """
        Return the weight matrix.

        Returns
        -------
        self.weights
            List of lists of floats representing individual weights.

        """
        return self.weights

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

        with open(path_to_output, 'w', encoding='utf-8') as csv_file:
            # Initialize the writer of the CSV file
            csv_writer: _csv._writer = csv.writer(csv_file)

            # Clear the file if it already existed
            if file_exists:
                csv_file.truncate(0)

            # Write each weight matrix
            for matrix in weight_matrices:
                csv_writer.writerow(matrix.get_weights())
