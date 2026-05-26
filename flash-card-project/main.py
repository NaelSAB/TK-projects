from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    DATA = pandas.read_csv("./data/words_to_learn.csv", encoding="utf-8")

except FileNotFoundError:
    DATA = pandas.read_csv("./data/arabic_words.csv", encoding="utf-8")

finally:
    to_learn = DATA.to_dict(orient="records")


# ---------------------------- IS RIGHT ------------------------------- #

def is_right():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", encoding="utf-8", index=False)

    next_card()


# ---------------------------- NEW FLASH CARDS ------------------------------- #

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=front_card_image)
    canvas.itemconfig(label_title, text="Arabic", fill="black")
    canvas.itemconfig(label_Word, text=current_card["Arabic"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- FLIP CARD ------------------------------- #

def flip_card():
    canvas.itemconfig(card_image, image=back_card_image)
    canvas.itemconfig(label_title, text="English", fill="white")
    canvas.itemconfig(label_Word, text=current_card["English"], fill="white")

# ---------------------------- UI SETUP ------------------------------- #

#Window:
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#Image:
front_card_image = PhotoImage(file="./images/card_front.png")
back_card_image = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

#Canves:
canvas = Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400,263, image=front_card_image)
label_title = canvas.create_text(400,150, text="", font=("Ariel", 40, "italic"))
label_Word = canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column= 0, row= 0, columnspan=2)

#Labels:

#Entrys:

#Buttons:
button_right = Button(image=right_image, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR, command=is_right)
button_right.grid(column=1, row=1)
button_wrong = Button(image=wrong_image, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR, command=next_card)
button_wrong.grid(column=0, row=1)

next_card()

window.mainloop()