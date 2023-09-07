# import all functions from the tkinter
import tkinter as tk
from tkinter import *

# import messagebox class from tkinter
from tkinter import messagebox
# global list is declare for storing all the task
tasks_list = []
# global variable is declare for counting the task
counter = 1
# Function for checking input error when  empty input is given in task field

def inputError() :
	# check for enter task field is empty or not
	if enterTaskField.get() == "" :
		# show the error message
		messagebox.showerror("Input Error")
		return 0
	return 1
# Function for clearing the contents  of task number text field

def clear_taskNumberField() :
	# clear the content of task number text field
	taskNumberField.delete(0.0, END)
# Function for clearing the contents of task entry field

def clear_taskField() :
# clear the content of task field entry box
	enterTaskField.delete(0, END)	
# Function for inserting the contents from the task entry field to the text area

def insertTask():
	global counter
	# check for error
	value = inputError()
	# if error occur then return
	if value == 0 :
		return
	# get the task string concatenating  with new line character
	
	content = enterTaskField.get() + "\n"
	# store task in the list
	tasks_list.append(content)
	# insert content of task entry field to the text area add task one by one in below one by one
	
	TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
	# incremented
	counter += 1
	# function calling for deleting the content of task field
	clear_taskField()
# function for deleting the specified task
def delete() :
	global counter
	# handling the empty task error
	if len(tasks_list) == 0 :
		messagebox.showerror("No task")
		return
        # get the task number, which is required to delete
	number = taskNumberField.get(1.0, END)

	# checking for input error when  empty input in task number field
	
	if number == "\n" :
		messagebox.showerror("input error")
		return
	else :
		task_no = int(number)
	# function calling for deleting the content of task number field
	clear_taskNumberField()
	# deleted specified task from the list
	tasks_list.pop(task_no - 1)
	# decremented
	counter -= 1
	# whole content of text area widget is deleted
	TextArea.delete(1.0, END)
	# rewriting the task after deleting one task at a time
	for i in range(len(tasks_list)) :
		TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])
# Driver code
if __name__ == "__main__" :

	# create a GUI window
	gui = Tk()

	# set the background colour of GUI window
	gui.configure(background = "purple")

	# set the title of GUI window
	gui.title("ToDo App by JITHENDRA KUMAR")

	# set the configuration of GUI window
	gui.geometry("780x280+300+200")
	gui.resizable(False,False)
	image_icon = tk.PhotoImage(file="Image/topbar.png")
	icon=tk.Label(gui, image=image_icon, bg="#32405b").place(x=0, y=0)
        
        
	

	# create a label : Enter Your Task
	enterTask = Label(gui, text = "Enter Your Task :)) ",font=("Lucida",10,"bold"))

	# To create a text entry box for typing the task
	enterTaskField = Entry(gui)
	enterTaskField.configure(font=("Lucida",12,'bold'),bg='blue',fg='white')
	# grid method is used for placing the widgets at respective positions in table like structure.
	enterTask.grid(row = 0, column = 1)

	# ipadx attributed set the entry box horizontal size			
	enterTaskField.grid(row = 0, column = 2, ipadx = 50,ipady=3)
        
	# create a Submit Button and place into the root window when user press the button,
	# the command or function affiliated to that button is executed
	
        #To-do list visible
	todolist=Label(gui,text="---YOUR TO-DO List----",font=("Lucida",10,"bold"))
	todolist.grid(row=3,column=2)
	
	#icon.grid(row=0,column=0,padx=10,sticky=W,ipadx=10,pady=10)
	# Icon
        
       

	# create a text area for the root with lunida 13 font text area is for writing the content
	TextArea = Text(gui, height = 6, width = 25, font = "lucida 13")
	TextArea.configure(font=("Areial",12,'bold'),foreground='blue')
	TextArea.grid(row = 4, column = 2, padx = 10, sticky = W)
	#finished tasks 
	finish = Label(gui, text = "Delete the Completed Tasks", font=("Lucida",10,"bold"))
	finish.grid(row = 6, column = 2)
	
	# create a label : Delete Task Number
	taskNumber = Label(gui, text = "Completed-Task Number:", font=("Lucida",10,"bold"))
	# padx attributed provide x-axis margin from the root window to the widget
	# pady attributed provide y-axis margin from the widget.
	taskNumber.grid(row = 8, column = 1, ipadx = 5,ipady=2)
	
	taskNumberField = Text(gui, height = 1, width = 3, font = "lucida 13")
	taskNumberField.grid(row = 8, column = 2,ipadx=100,ipady=2)
	dock_image = tk.PhotoImage(file="Image/task.png")
	dock=tk.Label(gui, image=dock_image, bg="#32405b").place(x=500, y=0)
        #dock
# create a Delete Button and place into the root window when user press the button,
 #the command or function affiliated to that button is executed .
	

	# create a Exit Button and place into the root window when user press the button,
	# #the command or function affiliated to that button is executed .
	delete = Button(gui, text = "Delete", fg = "Black", bg = "Red",borderwidth=3,border=2, command = delete)
	Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", borderwidth=3,border=2,command = exit)
	Submit = Button(gui, text = "Submit", fg = "Black", bg = "Red", borderwidth=3,border=2,command = insertTask)
	Submit.grid(row = 0, column = 3)
	delete.grid(row = 8, column = 3, pady = 5)
						
	Exit.grid(row = 10, column = 2)
        # start the GUI
	gui.mainloop()

