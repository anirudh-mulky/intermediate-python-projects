from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timertext,text = "00:00")
    timer_label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    worksec = WORK_MIN*60
    shortbreaksec = SHORT_BREAK_MIN*60
    longbreaksec = LONG_BREAK_MIN*60
    
    
    
    if reps%8==0:
        countdown(longbreaksec)
        timer_label.config(text="Break",fg=RED)
    elif reps%2==0:
        countdown(shortbreaksec)
        timer_label.config(text="Break",fg=PINK)
        
    else:
        countdown(worksec)
        timer_label.config(text="Work",fg=GREEN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0 or count_sec%10 == count_sec:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timertext, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,countdown, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(0,math.floor(reps/2)):
            mark += "✅"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



timer_label = Label(text="Timer",font=(FONT_NAME,40),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)


canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="/Users/anirudhmulky/Desktop/python/pomodoro-start/tomato.png")
canvas.create_image(100,112,image=tomato)
timertext = canvas.create_text(100,130,text = "00:00",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start = Button(text="Start",highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)


reset = Button(text="Reset",highlightthickness=0,command=reset)
reset.grid(column=2,row=2)

checkmark = Label(fg=GREEN,bg=YELLOW)
checkmark.grid(column=1,row=3)

window.mainloop()

