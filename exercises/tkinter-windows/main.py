import tkinter


# Do something when button is clicked
def button_clicked():
    print("Button clicked")
    # Get input field value with .get() , here  input (Entry class) is defined below as input = tkinter.Entry(width=10)
    new_text = input_field.get()
    my_label["text"] = new_text
    # or
    my_label.config(text=new_text)
    # my_label.place(x=100, y=100)


window = tkinter.Tk()
window.title("GUI program")
window.minsize(width=500, height=300)
# Add padding
window.config(padx=150, pady=130)

# Label
my_label = tkinter.Label(text="I am a label", font=("Verdana", 24, "bold"))
# Display label, .pack() centers it in the program.
my_label.grid(column=0, row=0)
# my_label.pack()

# Button
button = tkinter.Button(text="Click here", command=button_clicked)
button.grid(column=1, row=1)
# button.pack()

button2 = tkinter.Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)
# button.pack()


# Entry (input field)
input_field = tkinter.Entry(width=10)
input_field.grid(column=3, row=3)
# input_field.pack()

# Keep the window open
window.mainloop()
