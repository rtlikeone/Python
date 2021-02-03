import tkinter
from tkinter import messagebox
import string
import random
import pyperclip


# ---------------------------- CONSTANTS ------------------------------- #
ALPHABET_LOWER = string.ascii_lowercase
ALPHABET_UPPER = string.ascii_uppercase
ALPHABET = list(ALPHABET_LOWER + ALPHABET_UPPER)
NUMS = list(range(10))
SPECIAL_CHARS = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
NUMS_CHARS = ALPHABET + NUMS + SPECIAL_CHARS


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    """Generate random password.

    Args:
        None.

    Returns:
        - Handles the string value in the password input field after every "generate password" button click.
        - A password string consisting of lower- and uppercase letters, numbers and
        special characters (0-9) for up to 20 characters long.

    """
    password_input.delete(0, "end")
    password = ""
    for i in range(20):
        random_char = random.choice(NUMS_CHARS)
        password += str(random_char)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """Save data.

    Gets called whenever the add button is clicked. All the data entered in
    the website, username/email and password fields, are appended to data.txt.

    Args:
        None.

    Returns:
        - Shows a message box if empty fields detected.
        - Show a message box to confirm saving data to .txt file.
        - Opens the data.txt file using the .open() method and
        appends all the data gathered, using the .get() method, into this file.
        - Handles how the values that are entered are deleted from the
        input fields using the delete() method, after the add button is clicked.
    """
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops..",
            message="Please don't leave any fields empty.")
    else:
        # Output is a Boolean. Ok=True, Cancel=False
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\n"
                    f"Email: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode="a+") as datafile:
                datafile.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, "end")
                password_input.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, highlightthickness=10, highlightbackground="green")
window.resizable(False, False)

canvas = tkinter.Canvas(width=200, height=200)
password_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1, sticky="W")
email_username_label = tkinter.Label(text="Username:")
email_username_label.grid(column=0, row=2, sticky="W")
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3, sticky="W")

# Entries
website_input = tkinter.Entry()
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()
email_username_input = tkinter.Entry()
email_username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_username_input.insert(0, "email_address@gmail.com")
email_username_input.bind("<FocusIn>", lambda _: email_username_input.delete(0, "end"))
password_input = tkinter.Entry()
password_input.grid(column=1, row=3, sticky="EW")

# Buttons
generate_password = tkinter.Button(text="Generate password", command=gen_password)
generate_password.grid(column=2, row=3, sticky="EW")
add_new_user = tkinter.Button(text="Add", width=35, command=save_password)
add_new_user.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
