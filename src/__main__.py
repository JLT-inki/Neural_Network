"""Main file of the project."""

# Import used python libraries
import sys

# Import used classes
from classes.neural_network import NeuralNetwork
from classes.user_interface import UserInterface

# Size of the neural network
SIZE_NEURAL_NET: list[tuple[int, int]] = [(81, 784), (10, 81)]
# Path to the weight matrices
PATH_TO_WEIGHTS: str = "./weight_matrices/altered_weights.csv"

def main() -> int:
    """Show the user interface o the neural net."""
    # Set the CSV field size limit
    NeuralNetwork.set_csv_field_size()

    # Create the weights from the CSV file
    weights: list[list[list[float]]] = NeuralNetwork.create_weights_from_csv(
        PATH_TO_WEIGHTS)

    # Initialize the neural network
    neural_net: NeuralNetwork = NeuralNetwork(SIZE_NEURAL_NET, weights)

    # Initialize the user interface
    user_interface: UserInterface = UserInterface(neural_net)

    # Show the user interface
    user_interface.show_window()

    # Return exitcode 0 indicating success
    return 0


if __name__ == "__main__":
    sys.exit(main())
