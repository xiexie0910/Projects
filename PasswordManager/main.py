from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
FONT_NAME = "Courier"
WHITE = '#FFFFFF'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

     # randomly generate input rather than through user input
     nr_letters = random.randint(0,len(letters)-1)
     nr_symbols = random.randint(0,len(symbols)-1)
     nr_numbers = random.randint(0,len(numbers)-1)

     # generating the random letters, symbols and numbers 
     # ### the reason why random.randint(0,len(letters)-1) cannot be replaced by nr_letters is because they do not co exist
     password_letter = [(letters[random.randint(0,len(letters)-1)]) for _ in range(1, nr_letters)]
     password_symbol=[symbols[random.randint(0,len(symbols)-1)] for _ in range(1, nr_symbols)]
     password_number=[numbers[random.randint(0,len(numbers)-1)] for _ in range(1, nr_numbers)]

     password = list(password_letter + password_symbol + password_number)
     # randomly shuffling the string to imcrease the complexity of password
     random.shuffle(password)
     result = ''.join(password)
     # copying the password to clipboard
     pyperclip.copy(result)
     # clear entry and input the password
     password_entry.delete(0,END)
     password_entry.insert(0,result)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
     
     new_data={
          str(web_entry.get()).capitalize(): {
               "email": email_entry.get(),
               "password" : password_entry.get(),
          }
     }
     
     # pop up window response for different scenarios
     if web_entry.get() == '':
          messagebox.showwarning(title='Warning',message='Please enter a valid website')
     elif password_entry.get() == '':
          messagebox.showwarning(title='Warning',message='Please enter a valid password')
     else:
          try:
               # write the details to the json file
               with open(f"./password.json",'r') as password_txt:
                    
                    # reading old data
                    data = json.load(password_txt)
                    # update old data with new data
                    data.update(new_data)
                    

          except FileNotFoundError:
               with open(f"./password.json",'w') as password_txt:
                    # save updated data
                    json.dump(new_data, password_txt,indent=4)
          else:
               with open(f"./password.json",'w') as password_txt:
                    # save updated data
                    json.dump(data, password_txt,indent=4)
          finally:
               web_entry.delete(0,END)
               password_entry.delete(0,END)

# ---------------------------- SEARCH FOR A WEBSITE ------------------------------- #

def search():
     # try search through the json file
     try:
          with open(f"./password.json",'r') as password_txt:
                    # reading old data
                    data = json.load(password_txt)
                    messagebox.showinfo(title = "Website Information",
                                        message=f"Website: {str(web_entry.get()).capitalize()}\nEmail: {data[str(web_entry.get()).capitalize()]['email']}\nPassword: {data[str(web_entry.get()).capitalize()]['password']}")
     # catching the exceptions and displaying appropriate message
     except FileNotFoundError: 
          messagebox.showwarning(title='Warning',message='Please enter some details first')
     except KeyError:
          messagebox.showwarning(title='Warning',message='The website you entered cannot be found.')



# ---------------------------- UI SETUP ------------------------------- #

# creating an instance
window = Tk()
# title of the window
window.title("Password Manager")
# size of the window and the background color
window.config(padx=50,pady=50,bg='white')    


# size of the image, background color, and eliminating the border of the image
canvas = Canvas(width=200,height=200, highlightthickness=0,bg=WHITE) # highlightthickness eliminates the border of the tomato image
# imports the image file
logo_img = PhotoImage(file='logo.png')
# display the image on the window
canvas.create_image(100,100,image=logo_img) # x and y values are such that the image is bang on in the middle 
canvas.grid(row=0,column=1)

# set up the website label
web_label = Label(text='Website:',font=(FONT_NAME,10),bg=WHITE)
web_label.grid(row=1,column=0)
# set up the email label
email_label = Label(text='Email/Username:',font=(FONT_NAME,10),bg=WHITE)
email_label.grid(row=2,column=0)
# set up the password label
password_label = Label(text='Password:',font=(FONT_NAME,10),bg=WHITE)
password_label.grid(row=3,column=0)

# website entry
web_entry = Entry(width=21,bg=WHITE,highlightbackground=WHITE)
web_entry.grid(row=1,column=1)
web_entry.focus()
# email entry
email_entry = Entry(width=38,bg=WHITE,highlightbackground=WHITE)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(END, 'alexxienz02@gmail.com')
# password entry
password_entry = Entry(width=21,bg=WHITE,highlightbackground=WHITE)
password_entry.grid(row=3,column=1)     
# generate button for password
generate_button = Button(text='Generate Password', command=generate_password,highlightbackground=WHITE)
generate_button.grid(row=3,column=2)
# add button for additing to details to file
add_button = Button(text='Add', command=save_password,highlightbackground=WHITE,width=36)
add_button.grid(row=4,column=1,columnspan=2)

# add button for search details in the json file
add_button = Button(text='Search', command=search,highlightbackground=WHITE,width=13)
add_button.grid(row=1,column=2)


window.mainloop()
