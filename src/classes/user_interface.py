"""File containing the UserInterface class."""

# Import used Python libraries
import tkinter
import PIL

# Import used types
from tkinter import Button, Event, Canvas, Tk, Label
from PIL import Image as PILImage
from PIL import ImageDraw

# Import used classes
from classes.image import Image
from classes.neural_network import NeuralNetwork

# Constants for the images
PATH_TO_TRAINING_IMAGES: str = "./images/csv/training_data.csv"
PATH_TO_TESTING_IMAGES: str = "./images/csv/testing_data.csv"
# Path to the weight matrices
PATH_TO_WEIGHTS: str = "./weight_matrices/altered_weights.csv"

# Used learning rate
LEARNING_RATE: float = 0.001

class UserInterface:
    """
    A class representing the user interface of this project.

    Attributes
    ----------
    neural_net: NeuralNetwork
        The neural net through which the numbers shall be determined.
    main_window: Tk
        Main window on which all the other elements shall be displayed.
    drawing_pad: Canvas
        Canvas object on which the user can draw.
    previous_mouse_click: tuple[int, int]
        Last position (x, y) of the mouse on the canvas after a click.
    delete_button: Button
        Button to clear the drawing pad.
    submit_button: Button
        Button to submit the drawn number.
    created_image: PILImage
        Image that is created by drawing on the drawing pad.
    drawn_image: ImageDraw
        Image that is drawn.
    status_label: Label
        Label indicating the current status.
    training_button:
        Button to train the neural net.
    testing_button:
        Button to test the neural net.

    Methods
    -------
    set_neural_net
        Set the neural network of the user interface.
    set_main_window
        Set the main window of the user interface.
    set_drawing_pad
        Set the drawing pad of the user interface.
    set_previous_mouse_click
        Set the last position of the mouse on the canvas after a click.
    set_delete_button
        Set the button to clear the drawing pad.
    set_submit_button
        Set the button to submit the drawn number.
    set_created_image
        Set the image that is created by drawing on the drawing pad.
    set_drawn_image
        Set the image that is drawn.
    set_status_label
        Set the label indicating the current status.
    set_testing_button
        Set the button to train the neural net.
    set_testing_button
        Set the button to test the neural net.
    get_neural_net
        Return the neural network of the user interface.
    get_main_window
        Return the main window of the user interface.
    get_drawing_pad
        Return the drawing pad of the user interface.
    get_previous_mouse_click
        Return the last position of the mouse on the canvas after a click.
    get_delete_button
        Return the button to clear the drawing pad.
    get_submit_button
        Return the button to submit the drawn number.
    get_created_image
        Return the image that is created by drawing on the drawing pad.
    get_drawn_image
        Return the image that is drawn.
    get_status_label
        Return the label indicating the current status.
    get_training_button
        Return the button to train the neural net.
    get_testing_button
        Return the button to test the neural net.
    start_drawing
        Get the position (x, y) of a click on the canvas and set it.
    draw
        Draw on the canvas & the drawn image by following the mouse movement.
    clear_drawing_pad
        Clear the contents of the drawing pad.
    show_window
        Place all elements on the main window and show it.
    submit_number
        Submit the drawn number to the neural network.
    train
        Train the neural network.
    test
        Test the neural network.
    change_buttons
        Disable/Enables all buttons.
    update_status
        Update the status label on the window.

    """

    def __init__(self, neural_net: NeuralNetwork) -> None:
        """
        Construct one UserInterface object with the given attributes.

        Parameters
        ----------
        neural_net: NeuralNetwork
            The neural net through which the numbers shall be determined.

        """
        # Set the neural network
        self.set_neural_net(neural_net)

        # Initialize the main window
        self.set_main_window(tkinter.Tk())
        self.get_main_window().title("Neural Network")

        # Initialize the drawing pad
        self.set_drawing_pad(tkinter.Canvas(self.get_main_window(), width=224,
                                            height=224, background='white',))

        # Initialize the delete button of the drawing pad
        self.set_delete_button(tkinter.Button(self.get_main_window(), text="CLEAR",
                                              command=self.clear_drawing_pad))

        # Initialize the submit button of the drawing pad
        self.set_submit_button(tkinter.Button(self.get_main_window(), text="SUBMIT",
                                              command=self.submit_number))

        # Initialize the drawing image as well as the created image
        self.set_created_image(PIL.Image.new("RGB", (224, 224), "black"))
        self.set_drawn_image(ImageDraw.Draw(self.get_created_image()))

        # Initialize the label indicating the current status
        self.set_status_label(tkinter.Label(self.get_main_window(), width=26))

        # Initialize the buttons to train/test the neural net
        self.set_training_button(tkinter.Button(self.get_main_window(), text="TRAIN",
                                                command=self.train))
        self.set_testing_button(tkinter.Button(self.get_main_window(), text="TEST",
                                               command=self.test))

    def set_neural_net(self, neural_net: NeuralNetwork):
        """
        Set the neural network of the user interface.

        Parameters
        ----------
        neural_net: NeuralNetwork
            The neural net through which the numbers shall be determined.

        """
        self.neural_net: NeuralNetwork = neural_net

    def set_main_window(self, main_window: Tk) -> None:
        """
        Set the main window of the user interface.

        Parameters
        ----------
        main_window: Tk
            Main window on which all the other elements shall be displayed.

        """
        self.main_window: Tk = main_window

    def set_drawing_pad(self, drawing_pad: Canvas) -> None:
        """
        Set the drawing pad of the user interface.

        Additionally, two functions are binded to the canvas. The first one recognizes
        mouse clicks on the canvas. The second one enables drawing on it

        Parameters
        ----------
        drawing_pad: Canvas
            Canvas object on which the user can draw.

        """
        self.drawing_pad: Canvas = drawing_pad

        # Bind functions to the canvas to enable drawing
        self.drawing_pad.bind("<B1-Motion>", self.draw) 
        self.drawing_pad.bind("<Button-1>", self.start_drawing)

    def set_previous_mouse_click(self, previous_mouse_click: tuple[int, int]) -> None:
        """
        Set the last position of the mouse on the canvas after a click.

        Parameters
        ----------
        previous_mouse_click: tuple[int, int]
            Last position (x, y) of the mouse on the canvas after a click.

        Notes
        -----
        This setter is not called upon the initialization of the user interface,
        because this attribute shall only be set upon a mouse click.

        """
        self.previous_mouse_click: tuple[int, int] = previous_mouse_click

    def set_delete_button(self, delete_button: Button) -> None:
        """
        Set the button to clear the drawing pad.

        Parameters
        ----------
        delete_button: Button
            Button to clear the drawing pad.

        """
        self.delete_button: Button = delete_button

    def set_submit_button(self, submit_button: Button) -> None:
        """
        Set the button to submit the drawn number.

        Parameters
        ----------
        submit_button: Button
            Button to submit the drawn number.

        """
        self.submit_button: Button = submit_button

    def set_created_image(self, created_image: PILImage) -> None:
        """
        Set the image that is created by drawing on the drawing pad.

        Parameters
        ----------
        created_image: PILImage
            Image that is created by drawing on the drawing pad.

        """
        self.created_image: PILImage = created_image

    def set_drawn_image(self, drawn_image: ImageDraw) -> None:
        """
        Set the image that is drawn.

        Parameters
        ----------
        drawn_image: ImageDraw
            Image that is drawn.

        """
        self.drawn_image: ImageDraw = drawn_image

    def set_status_label(self, status_label: Label) -> None:
        """
        Set the label indicating the current status.

        Parameters
        ----------
        status_label: Label
            Label indicating the current status.

        """
        self.status_label: Label = status_label

    def set_training_button(self, training_button: Button) -> None:
        """
        Set the button to train the neural net.

        Parameters
        ----------
        training_button: Button
            Button to train the neural net.

        """
        self.training_button: Button = training_button

    def set_testing_button(self, testing_button: Button) -> None:
        """
        Set the button to test the neural net.

        Parameters
        ----------
        testing_button: Button
            Button to test the neural net.

        """
        self.testing_button: Button = testing_button

    def get_neural_net(self) -> NeuralNetwork:
        """
        Return the neural network of the user interface.

        Returns
        -------
        neural_net: NeuralNetwork
            The neural net through which the numbers shall be determined.

        """
        return self.neural_net

    def get_main_window(self) -> Tk:
        """
        Return the main window of the user interface.

        Returns
        -------
        main_window: Tk
            Main window on which all the other elements shall be displayed.

        """
        return self.main_window

    def get_drawing_pad(self) -> Canvas:
        """
        Return the drawing pad of the user interface.

        Returns
        -------
        drawing_pad: Canvas
            Canvas object on which the user can draw.

        """
        return self.drawing_pad

    def get_previous_mouse_click(self) -> tuple[int, int]:
        """
        Return the last position of the mouse on the canvas after a click.

        Returns
        -------
        previous_mouse_click: tuple[int, int]
            Last position (x, y) of the mouse on the canvas after a click.

        """
        return self.previous_mouse_click

    def get_delete_button(self) -> Button:
        """
        Return the button to clear the drawing pad.

        Returns
        -------
        delete_button: Button
            Button to clear the drawing pad.

        """
        return self.delete_button

    def get_submit_button(self) -> Button:
        """
        Return the button to submit the drawn number.

        Returns
        -------
        submit_button: Button
            Button to submit the drawn number.

        """
        return self.submit_button

    def get_created_image(self) -> PILImage:
        """
        Return the image that is created by drawing on the drawing pad.

        Returns
        -------
        created_image: PILImage
            Image that is created by drawing on the drawing pad.

        """
        return self.created_image

    def get_drawn_image(self) -> ImageDraw:
        """
        Return the image that is drawn.

        Returns
        -------
        drawn_image: ImageDraw
            Image that is drawn.

        """
        return self.drawn_image

    def get_status_label(self) -> Label:
        """
        Return the label indicating the current status.

        Returns
        -------
        status_label: Label
            Label indicating the current status.

        """
        return self.status_label

    def get_training_button(self) -> Button:
        """
        Return the button to train the neural net.

        Returns
        -------
        training_button: Button
            Button to train the neural net.

        """
        return self.training_button

    def get_testing_button(self) -> Button:
        """
        Return the button to test the neural net.

        Returns
        -------
        testing_button: Button
            Button to test the neural net.

        """
        return self.testing_button

    def start_drawing(self, mouse_click: Event) -> None:
        """
        Get the position (x, y) of a click on the canvas and set it.

        Parameters
        ----------
        mouse_click: Event
            Position on the canvas that was clicked.

        """
        self.set_previous_mouse_click((mouse_click.x, mouse_click.y))

    def draw(self, cursor_movement: Event) -> None:
        """
        Draw on the canvas & the drawn image by following the mouse movement.

        Parameters
        ----------
        cursor_movement: Event
            Tracked position of the moving cursor

        """
        # Get the current mouse position
        current_position: tuple[int, int] = (cursor_movement.x, cursor_movement.y)

        # Draw a line from the last recognized mouse position to the new one
        self.get_drawing_pad().create_line(
            self.get_previous_mouse_click()[0], self.get_previous_mouse_click()[1],
            current_position[0], current_position[1], width=24, fill="black",
            capstyle=tkinter.ROUND, smooth=True, splinesteps=36)

        # Draw the exact same on the drawing image
        self.get_drawn_image().line(
            [(self.get_previous_mouse_click()[0], self.get_previous_mouse_click()[1]),
             current_position[0], current_position[1]], width=24, fill="white")

        # Update the last recognized mouse position with the new one
        self.set_previous_mouse_click(current_position)

    def clear_drawing_pad(self) -> None:
        """Clear the contents of the drawing pad and the drawn image."""
        self.get_drawing_pad().delete("all")
        self.get_drawn_image().rectangle(
            (0, 0, 224, 224), fill=(0, 0, 0, 0))

        # Also clear the status label
        self.update_status("")

    def show_window(self) -> None:
        """Place all elements on the main window and show it."""
        self.get_status_label().grid(row=0, column=0, columnspan=2)
        self.get_drawing_pad().grid(row=0, column=2, columnspan=2)
        self.get_training_button().grid(row=1, column=0)
        self.get_testing_button().grid(row=1, column=1)
        self.get_delete_button().grid(row=1, column=2)
        self.get_submit_button().grid(row=1, column=3)
        self.get_main_window().mainloop()

    def submit_number(self) -> None:
        """Submit the drawn number to the neural network."""
        # Create a copy of the currently created image to perform operations on it
        image_resized: PILImage = self.get_created_image().copy()

        # Resize the image to 28x28 to fit the size of the neural net
        image_resized = image_resized.resize((28, 28))

        # Get the pixel values of the image
        pixels: list[float] = []
        for i in range(image_resized.size[0]):
            for j in range(image_resized.size[1]):
                pixels.append(float(image_resized.getpixel((j, i))[0]) / 255)

        # Create an object of the (custom) Image class
        # NOTE: The actual number is NOT set as it isn't needed here
        image: Image = Image(pixels, None)

        # Run the image through the net and get the values at the output layer
        result: list[float] = self.get_neural_net().detect_one_image(image)[2]

        # Convert the results into percent values with two digits
        result_as_percent: list[str] = ["Number\t\tPercent"]
        for count, value in enumerate(result):
            result_as_percent.append(
                str(count) + ":\t\t" + "{:.2f}".format(round(value[0] * 100, 2)))
        results_as_string: str = "\n".join(result_as_percent)

        # Place the results
        self.update_status(results_as_string)

    def train(self) -> None:
        """Train the neural network."""
        # Clear the status label and drawing pad
        self.clear_drawing_pad()

        # Get the training images
        training_images: list[Image] = Image.create_images_from_csv(
            PATH_TO_TRAINING_IMAGES)

        # Update the status label to indicate that the net is training
        self.update_status("Currently training...")

        # Disable all buttons
        self.change_buttons()

        # Perform the training
        self.get_neural_net().train(training_images, LEARNING_RATE, PATH_TO_WEIGHTS)

        # Update the status label indicating that the training has finished
        self.update_status("Finished training!")

        # Enable all buttons
        self.change_buttons()

    def test(self) -> None:
        """Test the neural network."""
        # Clear the status label and drawing pad
        self.clear_drawing_pad()

        # Get the testing images
        test_images: list[Image] = Image.create_images_from_csv(PATH_TO_TESTING_IMAGES)

        # Get the number of images to properly present the accuracy
        number_of_images: int = len(test_images)

        # Update the status label to indicate that the net is testing
        self.update_status("Currently testing...")

        # Disable all buttons
        self.change_buttons()

        # Test the neural net and get the accuracy
        accuracy: float = self.get_neural_net().test(test_images) / number_of_images

        # Display the accuracy
        self.update_status("Accuracy:\t" + str(accuracy) + "%")

        # Enable all buttons
        self.change_buttons()

    def change_buttons(self) -> None:
        """Disable/Enables all buttons."""
        # Boolean indicating whether to enable or disable all buttons
        if self.get_delete_button()["state"] == "normal":
            enable: bool = False
        else:
            enable: bool = True

        # Switch all buttons
        if enable:
            self.get_delete_button()["state"] = "normal"
            self.get_submit_button()["state"] = "normal"
        else:
            self.get_delete_button()["state"] = "disable"
            self.get_submit_button()["state"] = "disable"

    def update_status(self, text: str) -> None:
        """
        Update the status label on the window.

        Parameters
        ----------
        text: str
            To be displayed text on the label.

        """
        self.status_label.config(text=text)
        self.status_label.update()
