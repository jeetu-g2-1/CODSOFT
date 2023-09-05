# Python program to generate random
# password using Tkinter module
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk

# Function for calculation of password


def low():
	entry.delete(0, END)

	# Get the length of password
	length = var1.get()

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = ""

	# if strength selected is low
	if var.get() == 1:
		for i in range(0, length):
			password = password + random.choice(lower)
		return password

	# if strength selected is medium
	elif var.get() == 0:
		for i in range(0, length):
			password = password + random.choice(upper)
		return password

	# if strength selected is strong
	elif var.get() == 3:
		for i in range(0, length):
			password = password + random.choice(digits)
		return password
	else:
		print("Please choose an option")


# Function for generation of password
def generate():
	password1 = low()
	entry.insert(10, password1)


# Function for copying password to clipboard
def copy1():
	random_password = entry.get()
	pyperclip.copy(random_password)


# Main Function

# create GUI window
root = Tk()
var = IntVar()
var1 = IntVar()

# Title of your GUI window
root.title("Random Password Generator by JithendraKumar ")
root.configure(background='purple')
root.geometry('1200x350')
image_icon = tk.PhotoImage(file="Image/p1.png")
icon=tk.Label(root, image=image_icon, bg="#32405b").place(x=280, y=80)

# create label and entry to show
# password generated
Random_passwordl = Label(root, text="Password Generator ",font=('Lucida 13',25,'bold'),background='white',foreground='green')
Random_passwordl.grid(row=0,column=1,pady=9,padx=10)
Random_password = Label(root, text="Password: ",font=('Lucida 13',18,'bold'),foreground='green',background='white')
Random_password.grid(row=7)
entry = Entry(root,font=("Lucida",18,"bold"))
entry.grid(row=7, column=1,ipadx=90,ipady=4)

# create label for length of password
c_label = Label(root, text="Length: ",font=('Lucida 13',18,'bold'),foreground='green',background='white')
c_label.grid(row=2)




strength = Label(root, text="Range of Strength ",font=('Lucida 13',18,'bold'),foreground='orange',background='white')
strength.grid(row=3,column=1)

# create Buttons Copy which will copy
# password to clipboard and Generate
# which will generate the password
copy_button = Button(root, text="Copy", command=copy1 )
copy_button.grid(row=7, column=3)
generate_button = Button(root, text="Generate",command=generate,width=20)
generate_button.grid(row=7, column=2,padx=10)



        
# Radio Buttons for deciding the
# strength of password
# Default strength is Medium
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=4, column=1, padx=50,pady=10)
label1 = Label(root, text="(Lowercase letters) ",font=('Lucida 13',8,'bold'),foreground='green')
label1.grid(row=4,column=2)
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=5, column=1, padx=50,pady=10)
label1 = Label(root, text="(Lower&Uppercase letters) ",font=('Lucida 13',8,'bold'),foreground='green')
label1.grid(row=5,column=2)
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=6, column=1, padx=50,pady=10)
label1 = Label(root, text="(combination of lower,upper case alphabhets,digits,symbols) ",font=('Lucida 13',8,'bold'),foreground='green')
label1.grid(row=6,column=2)
combo = Combobox(root, textvariable=var1,font=("Lucida",18,'bold'))

# Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
				17, 18, 19, 20, 21, 22, 23, 24, 25,
				26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.configure(font=('Areial',20,'bold'),foreground="white")
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=2,ipadx=90,pady=9)

# start the GUI
root.mainloop()
