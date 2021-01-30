import tkinter


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
# bg of window
window.config(padx=100, pady=50, bg=YELLOW)

# Create canvas
# bg of cavas
canvas = tkinter.Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
# Photoimage reads through a file to get hold of the image
tomato_img = tkinter.PhotoImage(file="tomato.png")
# Define x and y coors. And the image itself
canvas.create_image(105, 112, image=tomato_img)
# Add text to display at an x and y value.
canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
# Show our canvas on screen
canvas.grid(column=1, row=1)

# Timer text label
timer_text = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45))
timer_text.grid(column=1, row=0)

# Start button
start_bt = tkinter.Button(text="Start")
start_bt.grid(column=0, row=2)

# Check mark label
check_mk = tkinter.Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28, "normal"))
check_mk.grid(column=1, row=3)

# Reset button
reset_bt = tkinter.Button(text="Reset")
reset_bt.grid(column=2, row=2)


window.mainloop()
