import tkinter
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data.csv")

# Create dict from our .csv file
# Converts the dict into a list: orient="records" => list like [{column -> value}, … , {column -> value}]
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    french = current_card["French"]
    canvas.itemconfig(canvas_img, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french, fill="black")
    timer = window.after(3000, show_translated)


def show_translated():
    english = current_card["English"]
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english, fill="white")


def is_known():
    # Remove from list if word is known. Rest of the words will be saved to: "words_to_learn.csv"
    # What's removed here is the random item in the to_learn list [{"French": "fr_word", "English": "en_word"}]
    # So current card equals: {"French": "fr_word", "English": "en_word"}
    to_learn.remove(current_card)
    print(len(to_learn))
    dict_to_dataframe = pandas.DataFrame(to_learn)
    dict_to_dataframe.to_csv("words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=20, bg=BACKGROUND_COLOR)
window.resizable(False, False)
# Wait 3s before flipping card
timer = window.after(3000, show_translated)

# Canvas to layer elements
canvas = tkinter.Canvas(width=800, height=526)
# Flash card images
front_img = tkinter.PhotoImage(file="img/card_front.png")
back_img = tkinter.PhotoImage(file="img/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_img)
# back_img_en = canvas.create_image(400, 263, image=back_img)

# Labels/Text
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, columnspan=2, row=0)


# Buttons/images
unknown_btn_img = tkinter.PhotoImage(file="img/wrong.png")
unknown_btn = tkinter.Button(image=unknown_btn_img, highlightthickness=0, command=next_card)
unknown_btn.grid(column=0, row=1)

correct_btn_img = tkinter.PhotoImage(file="img/right.png")
correct_btn = tkinter.Button(image=correct_btn_img, highlightthickness=0, command=is_known)
correct_btn.grid(column=1, row=1)

next_card()

window.mainloop()
