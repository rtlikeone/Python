import tkinter
# import pandas

# Read csv file
# data = pandas.read_csv("data.csv")
# Check attributes
# print(data)
# dataF = pandas.DataFrame(data)

# print(dataF)

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.resizable(False, False)

canvas = tkinter.Canvas(width=600, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
# bg_img = tkinter.PhotoImage(file="")
# canvas.create_image(300, 262, image=bg_img)
canvas.grid(column=2, row=0)

# Flash card images
front_img = tkinter.PhotoImage(file="img/card_front.png")
canvas.create_image(300, 200, image=front_img)
back_img = tkinter.PhotoImage(file="img/card_back.png")
canvas.create_image(300, 200, image=back_img)
canvas.grid(column=0, row=0)


window.mainloop()
