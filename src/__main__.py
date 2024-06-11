"""Main file of the project."""

# Import used python libraries
import sys

# Import used classes
from classes.neural_network import NeuralNetwork
from classes.image import Image

# Global constants
# ===================================================================
# Indicator whether to train or to test the neural network
TRAINING: bool = False
# Rate by which the weights shall be changed
LEARNING_RATE: float = 0.001
# Size of the neural network
SIZE_NEURAL_NET: list[tuple[int, int]] = [(81, 784), (10, 81)]
# Path to files
PATH_TO_WEIGHTS: str = "./weight_matrices/altered_weights.csv"
PATH_TO_TRAINING_IMAGES: str = "./images/csv/training_data.csv"
PATH_TO_TESTING_IMAGES: str = "./images/csv/testing_data.csv"

def main() -> int:
    """Train/Test the neural network."""
    # Set the CSV field size limit
    NeuralNetwork.set_csv_field_size()

    # Create the weights from the CSV file
    weights: list[list[list[float]]] = NeuralNetwork.create_weights_from_csv(
        PATH_TO_WEIGHTS)

    # Initialize the neural network
    neural_net: NeuralNetwork = NeuralNetwork(SIZE_NEURAL_NET, weights)

    # perform the training/testing
    if TRAINING:
        training_images: list[Image] = Image.create_images_from_csv(
            PATH_TO_TRAINING_IMAGES)
        neural_net.train(training_images, LEARNING_RATE, PATH_TO_TRAINING_IMAGES)
    else:
        test_images: list[Image] = Image.create_images_from_csv(PATH_TO_TESTING_IMAGES)
        accuracy: float = neural_net.test(test_images)
        print("Accuracy: ", accuracy)

    # Return exitcode 0 indicating success
    return 0


if __name__ == "__main__":
    sys.exit(main())
