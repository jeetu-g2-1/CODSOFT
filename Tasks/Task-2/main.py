# calculator using Tkinter
# import everything from tkinter module
from tkinter import *
# globally declare the expression variable
expression = ""
# Function to update expression
# in the text entry box
def press(num):
	# point out the global expression variable
	global expression
	# concatenation of string
	expression = expression + str(num)
	# update the expression by using set method
	equation.set(expression)
# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used for handling the errors like zero,division error etc.
	try:

		global expression
# eval function evaluate the expression and str function convert the result into string
		total = str(eval(expression))

		equation.set(total)

		# initialize the expression variable
		# by empty string
		expression = ""

	# if error is generate then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents
# of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	# create a GUI window
	gui = Tk()

	# set the background colour of GUI window
	gui.configure(background="grey")

	# set the title of GUI window
	gui.title("Simple Calculator by GEDDAM JITHENDRAKUMAR")

	# set the configuration of GUI window
	gui.geometry("610x600")

	# StringVar() is the variable class we create an instance of this class
	
	equation = StringVar()

	# create the text entry box for  showing the expression .
	
	expression_field = Entry(gui, textvariable=equation,font=("Lucida",18,"bold"))

	# grid method is used for placing the widgets at respective positions in table like structure .
	
	
	expression_field.grid(columnspan=5, ipadx=120,ipady=19)

	# create a Buttons and place at a particular location inside the root window.when user press the button, the command or
	#function affiliated to that button is executed .
	
	
	
	button1 = Button(gui, text=' 1 ', fg='white', bg='green',
				        command=lambda: press(1), font=("Lucida",18,"bold"),height=3, width=7,border=6,borderwidth=3)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='white', bg='green',
					command=lambda: press(2),font=("Lucida",18,"bold"), height=3, width=7,border=6,borderwidth=3)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='white', bg='green',
					command=lambda: press(3), font=("Lucida",18,"bold"),height=3, width=7,border=6,borderwidth=3)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='white', bg='green',
					command=lambda: press(4), font=("Lucida",18,"bold"),height=3, width=7,border=6,borderwidth=3)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='white', bg='green',
					command=lambda: press(5), font=("Lucida",18,"bold"),height=3, width=7,border=6,borderwidth=3)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='white', bg='green',
					command=lambda: press(6),font=("Lucida",18,"bold"), height=3, width=7,border=6,borderwidth=3)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='white', bg='green',
					command=lambda: press(7), font=("Lucida",18,"bold"),height=3, width=7,border=6,borderwidth=3)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='white', bg='green',
					command=lambda: press(8),font=("Lucida",18,"bold"), height=3, width=7,border=6,borderwidth=3)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='white', bg='green',
					command=lambda: press(9),font=("Lucida",18,"bold"), height=3, width=7,border=6,borderwidth=3)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='white', bg='green',
					command=lambda: press(0), font=("Lucida",18,"bold"),height=3, width=7,border=6,borderwidth=3)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='red',
				command=lambda: press("+"), font=("Lucida",18,"bold"),height=3, width=7,border=6,borderwidth=3)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='red',
				command=lambda: press("-"),font=("Lucida",18,"bold"), height=3, width=7,border=6,borderwidth=3)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='red',
					command=lambda: press("*"),font=("Lucida",18,"bold"), height=3, width=7,border=6,borderwidth=3)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='red',
					command=lambda: press("/"), font=("Lucida",18,"bold"),height=3, width=7,border=6,borderwidth=3)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='red',
				command=equalpress,font=("Lucida",18,"bold"), height=3, width=7,border=6,borderwidth=3)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='red',
				command=clear,font=("Lucida",18,"bold"), height=3, width=7,border=6,borderwidth=3)
	clear.grid(row=6, column='0')

	Decimal= Button(gui, text='.', fg='black', bg='red',
					command=lambda: press('.'),font=("Lucida",18,"bold"),height=3, width=7,border=6,borderwidth=3)
	Decimal.grid(row=5, column=1)
	# start the GUI
	gui.mainloop()
