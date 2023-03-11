from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
timer = None
count_tasks = 7
numdelete = 0
numcomplete=0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
     ''' resets labels and times to the default value'''
     window.after_cancel(timer)
     timer_label.config(text='Timer',fg=GREEN)
     tick_label.config(text='')
     canvas.itemconfig(timer_text,text="00:00")
     global reps
     reps = 0



# ---------------------------- CREATE TASK ------------------------------- # 

def create_task():
     global count_tasks,numdelete
     count_tasks +=1 
     
          
     #Entries
     entry = Entry(width=30,highlightbackground=YELLOW)
     #Add some text to begin with
     entry.insert(END, string=f"Task {count_tasks-7}: ")
     entry.grid(row=count_tasks,column=2)
           
     def delete_task():
          global numdelete,count_tasks,numcomplete
          entry.grid_remove()
          delete_task_button.grid_remove()
          numdelete +=1
          numcomplete +=1
          task_completed_label.config(text=f'{numcomplete} tasks completed')
          # if all the tasks are deleted, then the task count is resetted to 1
          if numdelete == count_tasks-7:
               count_tasks = 7
               numdelete = 0

     # setting up the create task button 
     delete_task_button = Button(text='Delete', highlightbackground=YELLOW, command=delete_task)
     delete_task_button.grid(row=count_tasks,column=3)
     

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
     '''starts the pomodoro timer'''
     global reps
     reps+=1
     if reps % 8 == 0:
          count_down(LONG_BREAK_MIN*60)
          timer_label.config(text='Break',fg=RED)
     elif reps % 2 == 0:
          count_down(SHORT_BREAK_MIN*60)
          timer_label.config(text='Break',fg=RED)
     else:
          count_down(WORK_MIN*60)  
          timer_label.config(text='Work',fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
     '''begin countdown'''
     count_min = floor(count/60)
     count_secs = int(count%60 )
     
     if count_secs < 10:
          count_secs = f"0{count_secs}"
     canvas.itemconfig(timer_text,text=f"{count_min}:{count_secs}")
     count = int(count)
     if count > 0:
          global timer
          timer = window.after(1000,count_down,count-1)
     else:
          start_timer()
          tick_label.config(text='✓'*floor(reps/2),fg=GREEN,bg=YELLOW)
               


# ---------------------------- UI SETUP ------------------------------- #

# creating an instance
window = Tk()
# title of the window
window.title("Pomodoro")
# size of the window and the background color
window.config(padx=200,pady=300,bg=YELLOW)    


# size of the image, background color, and eliminating the border of the image
canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0) # highlightthickness eliminates the border of the tomato image
# imports the image file
tomato_img = PhotoImage(file='tomato.png')
# display the image on the window
canvas.create_image(100,112,image=tomato_img)
# creating the text 
timer_text = canvas.create_text(103,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
# display the text
canvas.grid(row=2,column=2)


# set up the timer label
timer_label = Label(text='Timer',fg=GREEN,font=(FONT_NAME,35,'bold'),bg=YELLOW)
timer_label.grid(row=1,column=2)
# setting up the 2 buttons
start_button = Button(text='Start', command=start_timer,highlightbackground=YELLOW)
reset_button = Button(text='Reset', command=reset_timer,highlightbackground=YELLOW)
start_button.grid(row=3,column=1)
reset_button.grid(row=3,column=3)
# tick label set up
tick_label = Label(fg=GREEN,font=(FONT_NAME,30,'bold'),bg=YELLOW)
tick_label.grid(row=4,column=2)
# task_completed_label set up
task_completed_label = Label(text='0 tasks completed',fg=GREEN,font=(FONT_NAME,20),bg=YELLOW)
task_completed_label.grid(row=6,column=2)
# setting up the create task button     
create_task_button = Button(text='Create Tasks', highlightbackground=YELLOW, command=create_task)
create_task_button.grid(row=5,column=2)

window.mainloop()   