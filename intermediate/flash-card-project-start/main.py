from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
current_card = {} 

try:
    data = pandas.read_csv("/Users/anirudhmulky/Desktop/python/flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    original = pandas.read_csv("/Users/anirudhmulky/Desktop/python/flash-card-project-start/data/spanish.csv")
    to_learn = original.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="Spanish",fill="black")
    canvas.itemconfig(card_word,text = current_card["Spanish"],fill="black")
    canvas.itemconfig(card_background,image = card_front)
    window.after(4000, func=flip_card)
    timer = window.after(4000,func=flip_card)
def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text = current_card["English"],fill="white")
    canvas.itemconfig(card_background,image = card_back)
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

timer = window.after(4000, func=flip_card)

canvas = Canvas(width=800,height=526)
card_back = PhotoImage(file="/Users/anirudhmulky/Desktop/python/flash-card-project-start/images/card_back.png")
card_front = PhotoImage(file="/Users/anirudhmulky/Desktop/python/flash-card-project-start/images/card_front.png")
card_background = canvas.create_image(400,263,image = card_front)
card_title = canvas.create_text(400,150, text="",font=("Ariel",40,"italic"),fill="black")
card_word = canvas.create_text(400,263, text="",font=("Ariel",60,"bold"),fill="black")
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

cross_image = PhotoImage(file="/Users/anirudhmulky/Desktop/python/flash-card-project-start/images/wrong.png")
wrong_button = Button(image=cross_image,highlightthickness=0)
wrong_button.grid(row=1,column=0,)

check_image = PhotoImage(file="/Users/anirudhmulky/Desktop/python/flash-card-project-start/images/right.png")
right_button = Button(image=check_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

next_card()

window.mainloop()
