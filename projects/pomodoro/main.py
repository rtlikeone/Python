import tkinter
import math
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
ALARM = "alarm.mp3"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Reset the timer.

    The time will be reset to 00:00 after every reset button click.

    Args:
        None.

    Returns:
        - Updates reps.
        - Calls the window object: after_cancel method to cancel the timer delay.
        - Calls the canvas object: itemconfig method which takes the timer_text as a parameter
        and edits the text attribute for the canvas object.
        - Updates the timer_label text attribute.
        - Updates the check mark text attribute.
    """

    global reps
    reps = 0

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mk.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Start the timer.

    Args:
        None.

    Returns:
        - Updates reps
        - Calls the count_down() function for the subsequent amount of time equal
        for the work, short and long break pre-defined intervals, whenever the condition is met.
    """

    global reps
    reps += 1

    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    if reps % 8 == 0:
        playsound(ALARM)
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        print(f"LONG break! reps: {reps}")
    elif reps % 2 == 0:
        playsound(ALARM)
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
        print(f"SHORT break! reps: {reps}")
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        print(f"WORK! reps: {reps}")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Start the timer.

    Args:
        count: the specified amount of time pre-defined for work, a short- and long break.

    Returns:
        - Handles the display for minutes and secondes when < 10.
        - Updates the timer_label text attribute.
        - Handles the delay for the timer.
        - Updates the check mark text attribute.
    """

    minutes = math.floor(count / 60)
    seconds = count % 60

    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    # To edit a piece of text in a canvas (update time display), it differs from editing a label (.config).
    # For this we use a member of the Canvas class, the .itemconfig() member.
    # It takes the timer_text here as an argument and updates the display with count.

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count >= 0:
        global timer
        # The .after(ms. func, *args) executes a command after a time delay.
        # The timer first start as None but through the .after() is updated every 1000ms.
        # Which calls count_down() recursively and updates the count accordingly until the condition is False.
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmark = ""

        # Update checkmark after every work rep.
        for _ in range(math.floor(reps / 2)):
            checkmark += "✔"

        check_mk.config(text=checkmark)

        
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
# bg of window
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(False, False)

# Create canvas
# bg of canvas
canvas = tkinter.Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
# PhotoImage reads through a file to get hold of the image
tomato_img = tkinter.PhotoImage(file="tomato.png")
# Define x and y coors. And the image itself
canvas.create_image(105, 112, image=tomato_img)
# Add text to display at x and y coors.
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
# Show our canvas on screen
canvas.grid(column=1, row=1)

# Timer text label
timer_label = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45))
timer_label.grid(column=1, row=0)

# Start button
start_bt = tkinter.Button(text="Start", command=start_timer)
start_bt.grid(column=0, row=2)

# Check mark label
check_mk = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28, "normal"))
check_mk.grid(column=1, row=3)

# Reset button
reset_bt = tkinter.Button(text="Reset", command=reset_timer)
reset_bt.grid(column=2, row=2)


window.mainloop()
