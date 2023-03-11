from tkinter import *
from tkinter import messagebox
from PIL import Image
from time import sleep
import random
import pyperclip
import json
import pandas
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- GENERATE WORD ------------------------------- # 

def word_learnt():
     global current_word,flip_timer
     # after_cancel() function stops the scheduling of the after() function so that it doesn't flip automatically after 3 secs
     window.after_cancel(flip_timer)
     if len(file) > 0:
          # this is a dictionary that stores a random word in french and english
          current_word = random.choice(file)
          # changing the canvas display using itemconfig
          canvas.itemconfig(french_label,text='French',fill='black')
          canvas.itemconfig(french_word,text=current_word['French'],fill='black')
          canvas.itemconfig(card_background,image = logo_img)
          # storing the word into the knowns_word dictioanry
          file.remove(current_word)

          words_to_learn = pd.DataFrame(file)
          words_to_learn.to_csv('data/words_to_learn.csv')   
          
          # start after timer of 3 seconds to flip the card
          flip_timer = window.after(3000,func=flip_card)
     else:
          # if the user memorises all the cards then execute the following command
          canvas.itemconfig(french_label,text='',fill='black')
          canvas.itemconfig(french_word,text='',fill='black')
          canvas.create_text(400,263,text='Congradulations, you memorised all the words',font=("Ariel",40,"italic",'bold')) 

def word_notlearnt():
     global current_word,flip_timer
     # after_cancel() function stops the scheduling of the after() function so that it doesn't flip automatically after 3 secs
     window.after_cancel(flip_timer)
     if len(file) > 0:
          # this is a dictionary that stores a random word in french and english
          current_word = random.choice(file)
          # changing the canvas display using itemconfig
          canvas.itemconfig(french_label,text='French',fill='black')
          canvas.itemconfig(french_word,text=current_word['French'],fill='black')
          canvas.itemconfig(card_background,image = logo_img)
          # start after timer of 3 seconds to flip the card
          flip_timer = window.after(3000,func=flip_card)
     else:
          pass
     
# ---------------------------- FLIP CARD ------------------------------- # 

def flip_card():
     if len(file)>0:
          # changes all the words to english and the background image
          canvas.itemconfig(french_label,text='English',fill='white')
          canvas.itemconfig(french_word,text=current_word['English'],fill='white')
          canvas.itemconfig(card_background,image = new_image)
     else:
          pass
     
     
# ---------------------------- UI SETUP ------------------------------- # 
try:
     # using pandas to read csv
     file = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
     file = pandas.read_csv('data/french_words.csv')
     file = file.to_dict('records') # records helps us determine which format to store the data
else:
     file = file.to_dict('records') # records helps us determine which format to store the data

current_word = {}


# creating an instance
window = Tk()
# title of the window
window.title("Password Manager")
# size of the window and the background color
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)    
# the window will execute the flip_card() function after 3000ms
flip_timer =window.after(3000,func=flip_card)

# size of the image, background color, and eliminating the border of the image
canvas = Canvas(width=800,height=526, highlightthickness=0,bg=BACKGROUND_COLOR) # highlightthickness eliminates the border of the tomato image
# imports the image file
logo_img = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
# display the image on the window
card_background = canvas.create_image(400,263,image=logo_img) # x and y values are such that the image is bang on in the middle 
french_label = canvas.create_text(400,150,text='French',font=("Ariel",40,"italic")) 
french_word = canvas.create_text(400,263,text='',font=("Ariel",40,"italic",'bold')) 
canvas.grid(row=0,column=0,columnspan=2)
# importing the image and creating a button for that image
wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img,highlightthickness=0,command=word_notlearnt)
wrong_button.grid(row=1,column=0)
right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img,highlightthickness=0,command=word_learnt)
right_button.grid(row=1,column=1)

word_notlearnt()




window.mainloop()