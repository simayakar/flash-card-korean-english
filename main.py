from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
converted_data = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/ko-en.csv")
    converted_data = original_data.to_dict('records')
else:
    converted_data = data.to_dict('records')



def next_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(converted_data)
    canvas.itemconfig(card_word, text=random_word["Korean"], fill="black")
    canvas.itemconfig(card_title, text="Korean", fill="black")
    canvas.itemconfig(canvas_img, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_word, text=random_word["English"], fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(canvas_img, image=card_back)


def is_known():
    converted_data.remove(random_word)
    updated_data = pandas.DataFrame(converted_data)
    updated_data.to_csv("data/words_to_learn.csv", index=False)
    next_word()

window = Tk()
window.title("Flash Card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)




canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.gif")
card_back = PhotoImage(file="images/card_back.gif")
canvas_img = canvas.create_image(400, 263, image=card_front)



card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.gif")
button = Button(image=right_image, highlightthickness=0, command=is_known)
button.config(bg=BACKGROUND_COLOR)
button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.gif")
button2 = Button(image=wrong_image, highlightthickness=0, command=next_word)
button2.config(bg=BACKGROUND_COLOR)
button2.grid(row=1, column=1)


next_word()



window.mainloop()