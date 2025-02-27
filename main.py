import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #

BREAK_COLOR = "#D17D98"
POMODORO_COLOR = "#A7D129"
BG_COLOR = "#3E432E"

TIMER_TITLE_FONT = ("Courier", 50, "bold")
TIMER_TEXT_FONT = ("Courier", 35, "bold")
BTN_FONT = ("Arial", 10, "bold italic")
BTN_BG_COLOR = "#616F39"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_FILE = "tomato.png"

# ---------------------------- GLOBAL VARIABLES ------------------------------- #
reps = 0
timer = ""
count = 0
marks = ""
is_stopped = False
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down():
    global reps
    global count
    global marks
    minute = str(math.floor(count / 60)).zfill(2)
    seconds = str(count % 60).zfill(2)
    canvas.itemconfig(timer_text, text=f"{minute}:{seconds}")

    if count > 0:
        global timer
        count -= 1
        timer = window.after(1000, count_down)
    else:
        if reps % 2 != 0:
            marks += "✔"
            check_mark.config(text=marks)
        start_timer()



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_btn.grid_forget()
    stop_btn.grid(column=0, row=2, padx=15, pady=15)
    global reps
    global count
    global is_stopped

    if is_stopped:
        is_stopped = False
        count += 1
        count_down()
    else:
        reps += 1
        if reps % 8 == 0:
            timer_title.config(text="Long Break")
            count = LONG_BREAK_MIN * 60
            count_down()
            reps = 0
        elif reps % 2 == 0:
            timer_title.config(text="Short Break")
            count = SHORT_BREAK_MIN * 60
            count_down()
        else:
            timer_title.config(text="Pomodoro")
            count = WORK_MIN * 60
            count_down()


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    stop_btn.grid_forget()
    start_btn.grid(column=0, row=2, padx=15, pady=15)

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"{str(WORK_MIN).zfill(2)}:00")
    timer_title.config(text="Pomodoro")
    check_mark.config(text="")
    global reps
    global count
    global is_stopped
    global marks
    marks = ""
    is_stopped = False
    reps = 0
    count = 0


# ---------------------------- TIMER STOP ------------------------------- #

def stop_timer():
    stop_btn.grid_forget()
    start_btn.grid(column=0, row=2, padx=15, pady=15)
    window.after_cancel(timer)
    global is_stopped
    is_stopped = True

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pydoro")
window.config(padx=30, pady=30, bg=BG_COLOR)



timer_title = Label(text="Pomodoro", width= 11, bg=BG_COLOR, fg=POMODORO_COLOR, font=TIMER_TITLE_FONT)
timer_title.grid(column=0, row=0)

canvas = Canvas(width=200, height=224, bg=BG_COLOR, highlightthickness=0)
tomato_img = PhotoImage(file=TOMATO_FILE)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=f"{str(WORK_MIN).zfill(2)}:00", fill="white", font=TIMER_TEXT_FONT)
canvas.grid(column=0, row=1,)


btn_frame = Frame(window, bg=BG_COLOR)
btn_frame.grid(column=0, row=2)

start_btn = Button(btn_frame, width=7, text="Start", relief="groove", fg="white",bg = BTN_BG_COLOR, font=BTN_FONT, command=start_timer)
start_btn.grid(column=0, row=2, padx=15, pady=15)

stop_btn = Button(btn_frame, width=7, text="Stop", relief="groove", fg="white",bg = BTN_BG_COLOR, font=BTN_FONT, command=stop_timer)
stop_btn.grid_forget()

reset_btn = Button(btn_frame, width=7, text="Reset", relief="groove", fg="white",bg = BTN_BG_COLOR, font=BTN_FONT, command=reset_timer)
reset_btn.grid(column=1, row=2, padx=15, pady=15)

check_mark = Label(text="", fg=POMODORO_COLOR, bg=BG_COLOR, font=("Arial", 20))
check_mark.grid(column=0, row=3)





window.mainloop()