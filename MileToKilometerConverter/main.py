# importing modules
import tkinter
# creating a tk instance
window = tkinter.Tk()
# title and size
window.title("Miles to Kilometer Converter")
window.minsize(width=500,height=300)
# miles label
my_label = tkinter.Label(text='Mile',font=("Arial",20))
my_label.place(x=220,y=90)

# First entry
entry = tkinter.Entry(width=10)
# Add some text to begin with
entry.insert(tkinter.END, string="")
# placing it onto the screen 
entry.place(x=220,y=120)
# second text
my_label2 = tkinter.Label(text='is equal to',font=("Arial",15))
# placing it onto the screen 
my_label2.place(x=140,y=150)
# third text
km = tkinter.Label(text='km',font=("Arial",15))
# placing it onto the screen 
km.place(x=325,y=150)

# when the button is pretty this function will be called
def action():
     # set the text of the label as the result in km
     km.config(text=float(entry.get()) * 1.609)

# calls action() when pressed
button = tkinter.Button(text="Convert", command=action)
# placing it onto the screen 
button.place(x=220,y=180)
# fourth text
km = tkinter.Label(text='0',font=("Arial",15))
# placing it onto the screen 
km.place(x=220,y=150)




window.mainloop()