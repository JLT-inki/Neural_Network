"""File containing a function that sets the CSV field size."""

import sys
import csv

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
