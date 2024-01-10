"""File to initialize the weight matrices with values in the range of [0; 1]."""

import os
import sys
import random
import weight_matrix

# Path to the folder in which the weight matrices are saved as CSV files
MATRICES_PATH: str = "./weights"

# Dimensions of the weight matrices as list of tuples in the form of {rows, columns}
MATRICES_DIMENSIONS: list[tuple[int, int]] = [(784, 100), (100, 10)]

def main() -> int:
    """Create weight matrices with random values and save them in a CSV file."""
    try:
        # Check if weight matrices were already created
        folder_content = os.listdir(MATRICES_PATH)
        # It is checked for size == 1 to incorporate the .gitkeep file
        folder_empty: bool = len(folder_content) == 1

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
                        os.remove(MATRICES_PATH + "/" + file)
            # Aboard the script otherwise
            else:
                return 0

        weight_matrices: list[weight_matrix.WeightMatrix] = []

        for dimensions in MATRICES_DIMENSIONS:
            # Create random values in range of [0; 1] for the weight matrices
            values: list[list[float]] = [[
                random.random() for _ in range(dimensions[1])]
                for __ in range(dimensions[0])]

            weight_matrices.append(weight_matrix.WeightMatrix(values))

        # Write the weights into a csv file
        weight_matrix.WeightMatrix.write_weights(
            MATRICES_PATH + "/weight_matrices.csv", weight_matrices)

        # Return exitcode 0, indicating success
        return 0
    except FileNotFoundError:
        print(FileNotFoundError("Folder for weight matrices doesn't exist."))

        # Return exitcode 1, indicating failure
        return 1


if __name__ == "__main__":
    sys.exit(main())
