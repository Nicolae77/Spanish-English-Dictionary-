from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/spanish_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    print(current_card["English"])
    canvas.itemconfig(card_title, text="Spanish")
    canvas.itemconfig(card_word, text=current_card["Spanish"])



window = Tk()
window.title("Spanish-English")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

canvas = Canvas(width=256, height=197)
front_img = PhotoImage(file="images/front_card.png")
canvas.create_image(128, 100, image=front_img)
card_title = canvas.create_text(128, 20, text="Title", font=("Ariel", 10, "italic"))
card_word = canvas.create_text(128, 80, text="word", font=("Ariel", 15, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, width=120, height=110, command=next_card)
wrong_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, width=120, height=110, command=next_card)
check_button.grid(row=1, column=1)

next_card()
window.mainloop()
