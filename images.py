"""File containing the Image class."""

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
    tbd.

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

    @staticmethod
    def read_image_pixels(file: str) -> list[list[float]]:
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
            one image of 28x28 (784) pixels. The values are in range of [0; 1]

        Notes
        -----
        In the file the bytes are in range of [0; 255]. Since the output values of
        the neural network are values in range of [0; 1], the byte values are
        converted to be floats in that range. To do so they are divided by 255.

        """
        # Open the file
        with open(file, 'rb') as buffered_reader:
            # Ignore the first 16 bytes since the image bytes only start at offset 16
            images = list(buffered_reader.read()[16:])

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
            all_image_pixels[current_image_number].append(image_byte / 256)

        return all_image_pixels

    @staticmethod
    def read_image_labels(file: str) -> list[int]:
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
            representing the number that the 784 pixels represent

        """
        # Open the file
        with open(file, 'rb') as buffered_reader:
            # Ignore the first 8 bytes since the image labels only start at offset 8
            all_image_labels = list(buffered_reader.read()[8:])

        return all_image_labels
