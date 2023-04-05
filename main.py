BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
card_back_pic=None
enlish_word=None
car_front_pic=None
chosen_word={}

try:
  data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  original_data=pandas.read_csv("./data/french_words.csv")
  to_learn=original_data.to_dict(orient="records")
else:
  to_learn=data.to_dict(orient="records")
  

#print(to_learn)
#------------------------------------------------------------

def generate_word():
  global timer
  global english_word
  global car_front_pic
  global chosen_word
  canvas.itemconfig(canvas_image, image=card_front_pic)
   
  chosen_word=random.choice(to_learn)
  french_word=chosen_word["French"]
  english_word=chosen_word["English"]

  
  canvas.itemconfig(language_text, text="French", fill="black")
  canvas.itemconfig(translate_text, text=f"{french_word}", fill="black")

  timer=window.after(3000, translate)
  


#------------------------------------------------------------

def translate():

  global card_back_pic
  global timer
  #global english_word

  canvas.itemconfig(canvas_image, image=card_back_pic)
  

  canvas.itemconfig(language_text, text="English", fill="white")
  canvas.itemconfig(translate_text, text=f"{english_word}", fill="white")
  window.after_cancel(timer)

  
#-----------------------------------------------------------
def is_know():
  
  to_learn.remove(chosen_word)
  
  df = pandas.DataFrame(to_learn)
  df.to_csv("data/words_to_learn.csv", index=False)

  generate_word()





#--------------------------------------------------------------
window=Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas=Canvas(width=800, height=526, highlightthickness=0)
card_front_pic=PhotoImage(file="./images/card_front.png")
card_back_pic=PhotoImage(file="./images/card_back.png")

canvas_image=canvas.create_image(400, 270, image=card_front_pic)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

language_text=canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
canvas.grid(row=0, column=0)

translate_text=canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_know)
right_button.grid(row=1, column=1)


generate_word()


window.mainloop()
