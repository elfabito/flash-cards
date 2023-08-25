from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_L = ("Arial",40, "italic")
FONT = ("Arial",60, "bold")

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    data = pandas.read_csv("data/french_words.csv")

current = {}
dic = data.to_dict('records')

def wrong():
    next()
def approved():
    dic.remove(current)
    d = pandas.DataFrame(dic)
    a = d.to_csv()
    with open("data/words_to_learn.csv", "w") as file:
        file.write(a)
    next()
def next():
    global current, flip
    window.after_cancel(flip)
    current = random.choice(dic)
    words = current["French"]
    canvas.itemconfig(word, text=f"{words}", fill="#000000")
    canvas.itemconfig(title, text="French", fill="#000000")
    canvas.itemconfig(canvas_image, image=img_c)

    flip = window.after(3000, func=turn)

def turn():
    global canvas_image
    canvas.itemconfig(word, text=current["English"], fill="white")
    canvas.itemconfig(title, text="English", fill="white")

    canvas.itemconfig(canvas_image, image=img_b)



window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip = window.after(3000, func=turn)
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
img_c = PhotoImage(file="images/card_front.png")
img_b = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263, image= img_c)
title = canvas.create_text(400,150, text="Title", font=FONT_L, fill="#000000")
word = canvas.create_text(400,263, text="Word", font=FONT, fill="#000000")
canvas.grid(column=0,row=0, columnspan=2)



img_x = PhotoImage(file="images/wrong.png")
button_x = Button(image=img_x, highlightthickness=0, command=wrong)
button_x.grid(column=0, row=1)

img_g = PhotoImage(file="images/right.png")
button_g = Button(image=img_g, highlightthickness=0, command=approved)
button_g.grid(column=1, row=1)






next()







window.mainloop()


