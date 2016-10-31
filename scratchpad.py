
from Tkinter import *

fields = ("What is your outstanding balance? ", "What is your annual interest rate? ", 
	"How many months? ")

symbols = ("$", "%", "")

choices = (6, 12, 18, 24)

class Credit_Debt():
	def __init__(self, master, fields, symbols):
		self.master = master
		self.labelframe()
		self.topframe(fields, symbols)
		self.middleframe()
		self.buttonframe()

	def labelframe(self):
		label1 = Label(self.master, text = "Payoff Calculator", bg = "white", 
			anchor = "w", padx = 10, pady = 20, font = ("helvetica", 30))
		label1.pack(side = "top", fill = "x")

		label2 = Label(self.master, text = "What will it take to pay of my credit debt?", 
			bg = "cornflower blue", anchor = "w", padx = 10, pady = 10, fg = "white", font = ("helvetica", 15))
		label2.pack(side = "top", fill = "x")
                
		#label_frame = Frame(self.master, bg = "red")
		#abel_frame.pack(side = "top", fill = "x")
		#label1 = Label(label_frame, text = "Payoff Calculator", bg = "blue", anchor = "w")
		#label1.pack(side = "top", fill = "x")
		#label2 = Label(label_frame, text = "What will it take to pay of my credit debt?")
		#label2.pack(side = "top")

	def topframe(self, fields, symbols):
		self.entries = {}

		for (field, symbol) in zip(fields, symbols):
			top_frame = Frame(self.master, bg = "cornflower blue")
			top_frame.pack(side = "top", fill = "x")
			label = Label(top_frame, text = field, pady = 5, 
				padx = 10, anchor = "w", font = ("helvetica", 15))
			label.pack(side = "top", fill = "x")
			if field == "How many months? ":
				self.var = StringVar(top_frame)
				self.var.set("Months")
				dropdown = OptionMenu(top_frame, self.var, *choices)

				dropdown.pack(side = "top", fill = "x")
			else:
				symbollabel = Label(top_frame, text = symbol, fg = "white", bg = "cornflower blue", font = ("helvetica", 15),anchor = "w")
				symbollabel.pack(side = "left", fill = "x")
				entry = Entry(top_frame, bd = 0)
				entry.pack(side = "right", fill = "x",expand = True, padx = 3, pady = 3, ipadx = 1, ipady = 1)
				self.entries[field] = entry

	def middleframe(self):
		middle_frame = Frame(self.master)
		middle_frame.pack(side = "top")

		solution_display = Text(middle_frame)

	def buttonframe(self):
		button_frame = Frame(self.master)
		button_frame.pack(side = "top")

		button_frame = Button(button_frame, text = "Compute", command = self.solution)
		button_frame.pack(side = "top")

	def solution(self):
		#print float(self.entries["What is your outstanding balance? "].get())
		months = float(self.var.get())

root = Tk()
root.geometry("500x500")
root.title("Payoff Calculator")
app = Credit_Debt(root, fields, symbols)
root.mainloop()
