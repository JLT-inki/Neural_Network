"""File containing the Image class."""

# Import necessary for create_images_from_csv method
from __future__ import annotations

import csv
import _csv

class Image:
    """
    A class representing one image.

    Attributes
    ----------
    pixels: list[float]
        The 28x28 (784) pixels of one image.
    actual_number: int
        The actual number that is drawn on the image.

    Methods
    -------
    get_pixels
        Return the pixels of the image.
    get_actual_number
        Return the actual number of the image.
    read_image_pixels_from_idx
        Read the image bytes from an IDX file.
    read_image_labels_from_idx
        Read the image labels from an IDX file.
    save_image_bytes_and_labels
        Read the image bytes and labels from an IDX file & save them in a CSV file.
    initialize_training_and_testing_data
        Read both training & testing images from IDX and save them in CSV files.

    """

    def __init__(self, pixels: list[float], actual_number: int) -> None:
        """
        Construct one Image object with the given attributes.

        Parameters
        ----------
        pixels: list[float]
            The 28x28 (784) pixels of one image.
        actual_number: int
            The actual number that is drawn on the image.

        """
        self.pixels = pixels
        self.actual_number = actual_number

    def get_pixels(self) -> list[float]:
        """
        Return the pixels of the image.

        Returns
        -------
        self.pixels
            The 28x28 (784) pixels of one image.

        """
        return self.pixels

    def get_actual_number(self) -> int:
        """
        Return the actual number of the image.

        Returns
        -------
        self.actual_number
            The actual number that is drawn on the image.

        """
        return self.actual_number

    @staticmethod
    def read_image_pixels_from_idx(file: str) -> list[list[float]]:
        """
        Read the image bytes from an IDX file.

        Parameters
        ----------
        file: str
            Path to the IDX file as a string.

        Returns
        -------
        all_image_pixels: list[list[float]]
            A List containing lists of 784 floats, with each list representing
            one image of 28x28 (784) pixels. The values are in range of [0; 1].

        Notes
        -----
        In the file the bytes are in range of [0; 255]. Since the output values of
        the neural network are values in range of [0; 1], the byte values are
        converted to be floats in that range. To do so they are divided by 255.

        """
        # Open the file
        with open(file, 'rb') as idx_file:
            # Ignore the first 16 bytes since the image bytes only start at offset 16
            images = list(idx_file.read()[16:])

        # Initialize the return value
        all_image_pixels: list[list[float]] = []

        # Count indicating the current image number
        current_image_number: int = -1

        for i, image_byte in enumerate(images):
            # Append a new list after every 784 bytes
            if i % 784 == 0:
                all_image_pixels.append([])

                # Increment the current image number
                current_image_number += 1

            # Append the converted byte
            all_image_pixels[current_image_number].append(image_byte / 255)

        return all_image_pixels

    @staticmethod
    def read_image_labels_from_idx(file: str) -> list[int]:
        """
        Read the image labels from an IDX file.

        Parameters
        ----------
        file: str
            Path to the IDX file as a string.

        Returns
        -------
        all_image_labels
            A list containing all the image labels. Each label is an integer
            representing the number that the 784 pixels represent.

        """
        # Open the file
        with open(file, 'rb') as idx_file:
            # Ignore the first 8 bytes since the image labels only start at offset 8
            all_image_labels = list(idx_file.read()[8:])

        return all_image_labels

    @staticmethod
    def save_image_bytes_and_labels(
        file_images: str, file_labels: str, path_to_output: str
    ) -> None:
        """
        Read the image bytes and labels from an IDX file & save them in a CSV file.

        Parameters
        ----------
        file_images: str
            Path to the file containing the bytes for the images.
        file_labels: str
            Path to the file containing the bytes for the image labels.
        path_to_output: str
            Path to the output file.

        """
        # Get the image labels and pixels
        all_image_labels = Image.read_image_labels_from_idx(file_labels)
        all_image_pixels = Image.read_image_pixels_from_idx(file_images)

        # Define the table header
        header = ['label', 'pixels']

        with open(path_to_output, 'w', encoding='utf-8') as csv_file:
            # Initialize the writer of the CSV file
            csv_writer: _csv._writer = csv.writer(csv_file)

            # Write the header
            csv_writer.writerow(header)

            # Iterate over all images
            for pixels, label in zip(all_image_pixels, all_image_labels):
                # Add the image label to the image pixels
                csv_writer.writerow([label, pixels])

    @staticmethod
    def create_images_from_csv(path_to_csv_file: str) -> list[Image]:
        """
        Read a CSV file and create an image per line that is read.

        Parameters
        ----------
        path_to_csv_file: str
            Path to the CSV file that is read.

        Returns
        -------
        image_list: list[Image]
            List containing all the images created.

        Notes
        -----
        The pixels are saved as string in the format of '[X.X, X.X, ..., X.X]'.
        To convert it into a list of floats, the first and last char are removed
        (the '[' and ']'). Afterwards they are split with teh separator ', ', to
        get a list of strings in the format of 'X.X'. Finally, they can then be
        converted to floats.

        Import in line 4 is necessary for type hints of this function as the type
        'Image' is used as a forward reference here (see index 563 of the
        Python Enhancement Proposals [PEP 563]).

        """
        # Initialize the return value
        image_list: list[Image] = []

        # Open the file
        with open(path_to_csv_file, 'r', encoding='utf-8') as csv_file:
            csv_reader: csv.DictReader = csv.DictReader(csv_file)

            # Read each row
            for row in csv_reader:
                # Read the label and convert it into an integer
                label = int(row['label'])

                # Read the pixels and convert it into a list of float
                pixels = [
                    float(pixel) for pixel in
                    row['pixels'][1:][:-1].split(', ')]

                # Create an image object and add it to the return value
                image_list.append(Image(pixels, label))

        # Return the list of all images created
        return image_list

    @staticmethod
    def initialize_training_and_testing_data(
        idx_path: str, csv_path: str, idx_files: list[tuple[str, str]], csv_files
    ) -> None:
        """
        Read both training & testing images from IDX and save them in CSV files.

        Parameters
        ----------
        idx_path: str
            Path to the folder in which the IDX files are stored.
        csv_path: str
            Path in which the CSV files shall be stored.
        idx_files: list[tuple[str, str]]
            Names of the IDX files. The first string of each tuple is the file
            containing the pixel values while the second file is the file containing
            the image labels, aka the actual numbers of the images.
        csv_files
            Names that the created CSV files shall have.

        """
        for idx_file, csv_file in zip(idx_files, csv_files):
            Image.save_image_bytes_and_labels(
                idx_path + idx_file[0], idx_path + idx_file[1],
                csv_path + csv_file)
