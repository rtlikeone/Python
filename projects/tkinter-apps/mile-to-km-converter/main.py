import tkinter


def reset_values():
    """Reset the text field and answer output values.

    The labels for the answer output as well as the value in the text field will be reset and
    cleared after every new option selected with the radio-buttons.

    Args:
        None.

    Returns:
        - Empty text field
        - Answer label reset to 0
    """
    return input_field.delete(0, "end"), answer.config(text="0")


def km_or_miles(radiobutton):
    """Listens for which radio-button is selected.

        After every radio-button selection this function will be triggered.
        It checks for the "text" key in the tkinter.Radiobutton dictionary.

        Args:
            radiobutton: gets the "text" key value for the tkinter.Radiobutton (radiobutton["text"])

        Returns:
            - Calls reset_values()
            - Edits the text labels for miles and km.
            - Calls convert_distance() functions after the value is checked in a conditional statement.
            - Places the new button on screen using the grid layout manager.

        """
    miles_or_km = radiobutton["text"]

    if miles_or_km == "Miles to Km":
        reset_values()
        miles_label.config(text="Miles")
        km_label.config(text="Km")
        miles_button = tkinter.Button(text="Calculate", command=lambda: convert_distance(miles_or_km))
        miles_button.grid(column=1, row=3)

    elif miles_or_km == "Km to miles":
        reset_values()
        km_label.config(text="Miles")
        miles_label.config(text="Km")
        km_button = tkinter.Button(text="Calculate", command=lambda: convert_distance(miles_or_km))
        km_button.grid(column=1, row=3)


def convert_distance(check_selection="Miles to Km"):
    """Converts miles to km and vice versa.

        Gets called in the km_or_miles() function after the radio-button
        value is checked in a conditional statement.
        It uses a try/except ValueError block if string cannot be converted to float.

        Args:
            check_selection.

        Returns:
            - The calculated miles value.
            - The calculated km value.
            - "Invalid distance string if text field input is not equal to float"
        """
    try:
        input_value = float(input_field.get())
        km = input_value * 1.609344
        miles = input_value / 1.609344

        if check_selection == "Km to miles":
            return answer.config(text=f"{round(miles, 2)}")
        return answer.config(text=f"{round(km, 2)}")
    except ValueError:
        return answer.config(text=f"Invalid distance")


window = tkinter.Tk()
window.title("Miles to km converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

# Pick option to convert miles to km or vice versa
rb_state = tkinter.IntVar()
miles_rb = tkinter.Radiobutton(text="Miles to Km", value=1, variable=rb_state, command=lambda: km_or_miles(miles_rb))
km_rb = tkinter.Radiobutton(text="Km to miles", value=2, variable=rb_state, command=lambda: km_or_miles(km_rb))
miles_rb.grid(column=0, row=0)
km_rb.grid(column=1, row=0)

# Miles input field
input_field = tkinter.Entry(width=10)
input_field.grid(column=1, row=1)

# Miles label
miles_label = tkinter.Label(text="Miles", borderwidth=2, relief="ridge")
miles_label.grid(column=2, row=1)

# Is equal to label
is_equal_label = tkinter.Label(text="is equal to:")
is_equal_label.grid(column=0, row=2)

# Output miles label
answer = tkinter.Label(text="0")
answer.grid(column=1, row=2)

# Km label
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=2)

# Button
calculate_button = tkinter.Button(text="Calculate", command=convert_distance)
calculate_button.grid(column=1, row=3)

window.mainloop()
