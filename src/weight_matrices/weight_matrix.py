"""File containing methods to write and receive weight matrices from/to csv files."""

from pathlib import Path

import ast
import csv
import _csv


def write_weights(path_to_output: str,
                  weight_matrices: list[list[list[float]]]) -> None:
    """
    Write weight matrices into a CSV file.

    Parameters
    ----------
    path_to_output: str
        Path to the CSV file in which the weight matrices need to be written.
    weight_matrices: list[list[list[float]]]
        Altered/New weights that need to be saved.

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
            csv_writer.writerow([weight_matrix])

def create_weights_from_csv(path_to_csv_file: str) -> list[list[list[float]]]:
    """
    Read a CSV file and create a weight matrix per line that is read.

    Parameters
    ----------
    path_to_csv_file: str
        Path to the CSV file that is read.

    Returns
    -------
    weight_matrix_list: list[list[list[float]]]
        List containing all the weight matrices created.

    """
    # Initialize the return value
    weight_matrix_list: list[list[list[float]]] = []

    with open(path_to_csv_file, 'r', encoding='utf-8') as csv_file:
        # Initialize the reader of the CSV file
        csv_reader: csv.DictReader = csv.DictReader(csv_file)

        # Read each row
        for row in csv_reader:
            # Read the weight matrix & create a WeightMatrix object
            weight_matrix_list.append(ast.literal_eval(row["weights"]))

    # Return the newly created lists
    return weight_matrix_list
