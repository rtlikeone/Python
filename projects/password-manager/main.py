import tkinter
import string
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
letters = list(alphabet_lower + alphabet_upper)
nums = list(range(10))
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
nums_chars = nums + letters + special_chars


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
        random_char = random.choice(nums_chars)
        password += str(random_char)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


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
add_new_user = tkinter.Button(text="Add", width=35)
add_new_user.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
