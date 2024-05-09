"""File containing the NeuralNetwork class."""

#Import used Python libraries
import pathlib
import random
import sys
import csv
import ast
import os

# Import used classes
from classes.image import Image

# Import used types
from csv import DictReader
import _csv

# Define Euler's Number as a global constant
EULERS_NUMBER: float = 2.718281828459045

class NeuralNetwork:
    """
    TBD!!!!
    """

    def __init__(self, dimensions: list[tuple[int, int]],
                 weight_matrices: list[list[list[float]]]) -> None:
        """
        Construct one NeuralNetwork object with the given attributes.

        Parameters
        ----------
        dimensions: list[tuple[int, int]]
            The dimensions of the neural network. Each tuple represents the crossing
            of one layer to another. The first value represents the size of the input
            layer of those two, while the second value represents the output layer of
            those two.
        weight_matrices: list[list[list[float]]]
            The weight matrices of the neural network. Each weight matrix is a list
            of lists of floats that is used to calculate the input values of a layer
            with the output values of the prior layer.

        """
        self.set_dimensions(dimensions)
        self.set_weight_matrices(weight_matrices)

    def set_dimensions(self, dimensions: list[tuple[int, int]]) -> None:
        """
        TBD!!!
        """
        self.dimensions: list[tuple[int, int]] = dimensions

    def set_weight_matrices(self, weight_matrices: list[list[list[float]]]) -> None:
        """
        TBD!!!
        """
        self.weight_matrices: list[list[list[float]]] = weight_matrices

    def get_dimensions(self) -> list[tuple[int, int]]:
        """
        TBD!!!
        """
        return self.dimensions

    def get_weight_matrices(self) -> list[list[list[float]]]:
        """
        TBD!!!
        """
        return self.weight_matrices

    @staticmethod
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
        file_exists: bool = pathlib.Path(path_to_output).is_file()

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

    @staticmethod
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
            csv_reader: DictReader = csv.DictReader(csv_file)

            # Read each row
            for row in csv_reader:
                # Read the weight matrix & create a WeightMatrix object
                weight_matrix_list.append(ast.literal_eval(row["weights"]))

        # Return the newly created lists
        return weight_matrix_list

    @staticmethod
    def sigmoid_function(x_value: float) -> float:
        """
        Calculate the output value of a neuron by using the sigmoid function.

        The function is as follows: y = 1 / (1 + e^-x)

        Parameters
        ----------
        x_value: float
            Input value of the neuron.

        Returns
        -------
        y_value: float
            Output value of the neuron. Values are in range of [0; 1].

        """
        y_value: float = 1 / (1 + EULERS_NUMBER ** -x_value)

        return y_value

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    def detect_one_image(self, image: Image) -> list[list[float]]:
        """
        Run one image through the neural network and return the values ath each layer.

        Parameters
        ----------
        image: Image
            The image that is being run through the neural network.

        Returns
        -------
        values_at_each_layer: list[float]
            Output values at each layer. The values at index 0 are the output values
            of the input layer. The values at the last index are the output values of
            the output layer. The values in between are the values at the respective
            hidden layers.

        """
        # Apply the sigmoid function to the values at the input layer
        values: list[float] = [[NeuralNetwork.sigmoid_function(val)]
                               for val in image.get_pixels()]
        values_at_each_layer: list[list[float]] = [values]

        # Go through each layer transition
        for weight_matrix in self.get_weight_matrices():
            # Calculate the input values for the next layer
            input_values: list[float] = NeuralNetwork.matrix_multiplication(
                weight_matrix, values)

            # Apply the sigmoid function to get the output values of this layer
            values = [[NeuralNetwork.sigmoid_function(val[0])] for val in input_values]

            # Save the output values of the current layer
            values_at_each_layer.append(values)

        return values_at_each_layer

    def calculate_output_error(self, current_image: Image,
                               values: list[float]) -> list[float]:
        """
        TBD!!!
        """
        # Calculate the expected values
        expected_values: list[int] = [0 for _ in range(10)]
        expected_values[current_image.get_actual_number()] = 1

        # Calculate the error
        output_error: list[int] = [
            [expected_values[i] - values[i][0]] for i in range(10)]

        return output_error

    def calculate_errors_at_each_layer(
            self, current_image: Image,
            values_ate_each_layer: list[list[float]]) -> list[list[float]]:
            """
            TBD!!!
            """

            # Calculate the error at the output layer
            error_at_current_layer: list[float] = self.calculate_output_error(
                current_image, values_ate_each_layer[len(values_ate_each_layer) - 1])
            errors_at_each_layer: list[list[float]] = [error_at_current_layer]

            # Calculate the errors for the other layers
            for weight_matrix in reversed(self.get_weight_matrices()):
                error_at_current_layer = NeuralNetwork.matrix_multiplication(
                    NeuralNetwork.invert(weight_matrix), error_at_current_layer)
                errors_at_each_layer.insert(0, error_at_current_layer)

            return errors_at_each_layer

    def adjust_weight_matrices(self, values_at_each_layer: list[list[float]],
                               errors_at_each_layer: list[list[float]],
                               learning_rate: float) -> None:       
        """
        TBD!!!!
        """
        # Initialize the changes
        changed_weight_matrices: list[list[list[float]]] = []
        # Go through each layer
        for i in range(len(self.get_weight_matrices())):
            # Calculate Alpha * Ek * Ok * (1 - Ok)
            change_to_weight_matrix: list[list[float]] = [
                [learning_rate * (err[0] * val[0] * (1 - val[0]))]
                for err, val in zip(errors_at_each_layer[i + 1],
                                    values_at_each_layer[i + 1])]

            # Calculate Alpha * Ek * Ok * (1 - Ok) * Oj^T
            change_to_weight_matrix = NeuralNetwork.matrix_multiplication(
                change_to_weight_matrix, NeuralNetwork.invert(values_at_each_layer[i]))

            # Calculate the new values for the weight matrix
            changed_weight_matrices.append(NeuralNetwork.matrix_addition(
                self.get_weight_matrices()[i], change_to_weight_matrix))

        # Apply the changes
        self.set_weight_matrices(changed_weight_matrices)

    def guessed_image_is_correct(self, image: Image,
                                 values_at_output_layer: list[float]) -> bool:
        """
        TBD!!!
        """
        return (values_at_output_layer.index(max(values_at_output_layer)) ==
                image.get_actual_number())

    def train(self, training_data: list[Image], learning_rate: float,
              path_to_csv_file) -> None:
        """
        TBD!!!
        """
        for count, single_image in enumerate(training_data):
            # Print a message each one thousand image
            if count % 1000 == 0 and count != 0:
                break
                print("Elapsed", count, "images.")
            if count % 10 == 0:
                print(count)

            # Calculate the output values at each layer
            values_at_each_layer: list[list[float]] = self.detect_one_image(
                single_image)

            # Calculate the error at each layer
            errors_at_each_layer: list[list[float]] = self.calculate_errors_at_each_layer(
                single_image, values_at_each_layer)

            # Apply the changes to the weight matrices
            self.adjust_weight_matrices(values_at_each_layer,
                                        errors_at_each_layer, learning_rate)

        # Write the adjusted weights into the csv file
        NeuralNetwork.write_weights(path_to_csv_file, self.get_weight_matrices())

    def test(self, testing_data: list[Image]) -> int:
        """
        TBD!!!
        """
        # Initialize the return value
        correct_images: int = 0

        for count, single_image in enumerate(testing_data):
            # Print a message each one thousand image
            if count % 1000 == 0 and count != 0:
                print("Elapsed", count, "images.")

            # Calculate the output values at each layer
            values_at_each_layer: list[list[float]] = self.detect_one_image(
                single_image)

            if self.guessed_image_is_correct(
                single_image, values_at_each_layer[len(values_at_each_layer) - 1]):
                correct_images += 1

        return correct_images

    @staticmethod
    def set_csv_field_size() -> None:
        """
        Set the CSV field size.

        Notes
        -----
        This function is necessary to avoid the csv error: 'field larger than field limit'.
        Also, this functions works in a try except frame to avoid the stackoverflow error.

        """
        # Get the max possible size as an initial value
        field_size: int = sys.maxsize

        while True:
            try:
                # Try setting the field size
                csv.field_size_limit(field_size)

                # If the size can be set break from the while True loop
                break
            except OverflowError:
                # Reduce the size to one tenth to try avoiding the stackoverflow error
                field_size = int(field_size / 100)

    def xavier_initialization(self, matrix_path: str) -> None:
        """
        TBD.
        """
        # Check if weight matrices were already created
        folder_content = os.listdir(matrix_path)
        # It is checked for size == 1 to incorporate the .gitkeep file
        folder_empty: bool = len(folder_content) <= 1

        # If the folder is not empty, existing CSV files will be overwritten
        if not folder_empty:
            print("Weight matrices appear to be already initialized.",
                  "Initialization will overwrite them.")
            decision: str = input("Do you want to continue? [y/n]\t").lower()

            while decision not in ["y", "n"]:
                decision = input("Please enter either 'y' or 'n':\t").lower()

            # Delete existing files if input is yes
            if decision == "y":
                for file in folder_content:
                    # Keep the .gitkeep file
                    if file != ".gitkeep":
                        os.remove(matrix_path + "/" + file)
            # Aboard the script otherwise
            else:
                return 0

        weight_matrices: list[list[list[float]]] = []

        for dimensions in self.get_dimensions():
            variance = 1 / dimensions[1]
            # Create random values in range of [0; 1] for the weight matrices
            values: list[list[float]] = [[
                random.uniform(-variance, variance) / 10 for _ in range(dimensions[1])]
                for __ in range(dimensions[0])]

            weight_matrices.append(values)

        # Write the weights into a csv file
        NeuralNetwork.write_weights(matrix_path + "/weight_matrices.csv",
                                    weight_matrices)
