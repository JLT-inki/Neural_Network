"""File containing several transfer functions that used for the neural network."""

# Define Euler's Number as a global constant
EULERS_NUMBER: float = 2.718281828459045

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
