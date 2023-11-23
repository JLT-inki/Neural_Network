"""File to read the IDX input data and convert it into CSV files."""

import sys
import images

# Path to the sub dictionaries for the IDX & CSV (to be generated) files
IDX_PATH = "./input/idx/"
CSV_PATH = "./input/csv/"

# Names of the IDX & CSV (to be generated) files
IDX_FILES: list[tuple[str, str]] = [
    ("train-images.idx3-ubyte", "train-labels.idx1-ubyte"),
    ("t10k-images.idx3-ubyte", "t10k-labels.idx1-ubyte")
]
CSV_FILES: list[str] = ["training_data.csv", "testing_data.csv"]

def main() -> int:
    """Read the IDX files and save the data in CSV files."""
    try:
        images.Image.save_image_bytes_and_labels(
            IDX_PATH + IDX_FILES[0][0], IDX_PATH + IDX_FILES[0][1],
            CSV_PATH + CSV_FILES[0]
        )
        images.Image.save_image_bytes_and_labels(
            IDX_PATH + IDX_FILES[1][0], IDX_PATH + IDX_FILES[1][1],
            CSV_PATH + CSV_FILES[1]
        )

        # Return exitcode 0, indicating success
        return 0
    except FileNotFoundError:
        print(FileNotFoundError("IDX or CSV file/path doesn't exist."))

        # Return exitcode 1, indicating failure
        return 1


if __name__ == '__main__':
    sys.exit(main())
